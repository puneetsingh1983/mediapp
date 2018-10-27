# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import AppUserModelSerializer
from .models import AppUserModel
from commons.permissions import IsAdministrator, IsSelfOrIsAdministrator


# Create your views here.
class AppUserViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

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
        request_data.setdefault("is_staff", True)
        request_data.setdefault("is_admin", False)
        request_data.setdefault("user_type", 0)
        request_data.setdefault("user_status", 1)

        _user = AppUserModel.objects.create_user(**request_data)
        _user.save()
        return Response(data={'success': True}, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, pk=None):
        """Update details of given user"""
        target_user = self.get_object()
        request_data = request.data
        user_status = request_data.get('user_status')
        user_type = request_data.get("user_type")
        mobile = request_data.get("mobile")
        imei = request_data.get("imei")
        reason = request_data.get("reason_for_modification")
        if user_status:
            target_user.user_status = user_status
        if user_type:
            target_user.user_type = user_type
        if mobile:
            target_user.mobile = mobile
        if imei:
            target_user.imei = imei
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

    @action(methods=['get'], detail=False, url_name="is_registered")
    def is_registered(self, request):
        """Validate device. If device already registered then redirect to login screen"""

        imei = request.GET.get('imei')
        response_msg = {'is_registered': False}
        if imei and AppUserModel.objects.filter(imei=int(imei)).exists():
            response_msg = {'is_registered': True}

        return Response(data=response_msg, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        """Inactivate user"""

        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(data={'success': True}, status=status.HTTP_200_OK)



