# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings

from .serializers import AppUserModelSerializer
from .models import AppUserModel, DEFAULT_TYPE, PENDING_APPROVAL
from helper.permissions import IsAdministrator, IsSelfOrIsAdministrator
from mobile_verification.models import OTP


# Create your views here.
class AppUserViewSet(ModelViewSet):
    """
    Application user model
    """
    # TODO - ACCOUNT RESET

    queryset = AppUserModel.objects.all()
    serializer_class = AppUserModelSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        # List view is open for ADMIN only
        if not (isinstance(request.user, AppUserModel) and request.user.is_admin):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super(self.__class__, self).list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ('retrieve', 'update', 'destroy', 'partial_update', 'is_registered'):
            self.permission_classes = [IsAuthenticated, IsSelfOrIsAdministrator]
        elif self.action in ('activate_user',):
            self.permission_classes = [IsAuthenticated, IsAdministrator]
        return super(self.__class__, self).get_permissions()

    @transaction.atomic
    def create(self, request):
        """Create New User in system."""
        request_data = request.data

        # check if user is already registered
        try:
            AppUserModel.objects.get(
                Q(username=request_data.get('username')) | Q(mobile=request_data.get('mobile')))
            return Response(
                data={'success': False, 'error': 'User is already registered!'},
                status=status.HTTP_400_BAD_REQUEST)
        except AppUserModel.DoesNotExist:
            pass

        request_data.setdefault("is_staff", True)
        request_data.setdefault("is_admin", False)
        request_data.setdefault("user_type", DEFAULT_TYPE)
        request_data.setdefault("user_status", PENDING_APPROVAL)

        _user = AppUserModel.objects.create_user(**request_data)
        payload = api_settings.JWT_PAYLOAD_HANDLER(_user)
        token = api_settings.JWT_ENCODE_HANDLER(payload)

        # TODO - Generated OTP and send in email as well as on phone
        # TODO - Add one more field saying is_otp_verified
        OTP.create_new_send(_user.mobile, _user.username)

        return Response(
            data={'success': True, 'token': token, 'user': self.serializer_class(_user).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, pk=None):
        """Update details of given user"""
        target_user = self.get_object()
        request_data = request.data
        user_status = request_data.get('user_status')
        user_type = request_data.get("user_type")
        mobile = request_data.get("mobile")
        reason = request_data.get("reason_for_modification")

        if user_status:
            target_user.user_status = user_status

        if user_type:
            target_user.user_type = user_type

        if mobile:
            # TODO - if phone no changed then generate OTP and send for verification and set flag is_otp_verified false
            # TODO - if is_otp_verified is false in response mobile APP will present OTP box
            if target_user.mobile != mobile:
                # if mobile number is changed then need to generate and send OTP to verify new mobile number
                OTP.create_new_send(mobile, target_user.username)
                # reset verification flag
                target_user.is_otp_verified = False
            target_user.mobile = mobile

        if reason:
            target_user.reason_for_modification = reason

        target_user.save()
        return Response(data={'success': True}, status=status.HTTP_200_OK)

    @transaction.atomic
    @action(methods=['put'], detail=True, url_name="activate_user")
    def activate_user(self, request, pk=None):
        """Activate given user"""

        instance = self.get_object()
        instance.is_active = True
        instance.save()
        return Response(data={'success': True}, status=status.HTTP_200_OK)

    # @action(methods=['get'], detail=False, url_name="is_registered")
    # def is_registered(self, request):
    #     """Validate device. If device already registered then redirect to login screen"""
    #
    #     response_msg = {'is_registered': False}
    #     if imei and AppUserModel.objects.filter(imei=int(imei)).exists():
    #         response_msg = {'is_registered': True}
    #
    #     return Response(data=response_msg, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False, url_name="reset_password")
    def reset_password(self, request):
        """Reset password"""

        request_data = request.data
        try:
            instance = AppUserModel.objects.get(
                Q(id=request_data.get('id')) |
                Q(username=request_data.get('username')) |
                Q(mobile=request_data.get('mobile')))
            password = AppUserModel.objects.make_random_password()

            send_mail("Reset Password",
                      "Password has been reset for your account.\n"
                      "New Password: {}".format(
                          password,),
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_HOST_USER, 'puneetsingh1983@gmail.com'])

            instance.set_password(password)
            instance.save()
            return Response(
                data={'success': True, 'message': 'Password is reset and sent to registered email'},
                status=status.HTTP_200_OK)

        except AppUserModel.DoesNotExist:
            return Response(
                data={'success': False, 'error': 'Invalid inputs'},
                status=status.HTTP_400_BAD_REQUEST)


    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        """Inactivate user"""

        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(data={'success': True}, status=status.HTTP_200_OK)



