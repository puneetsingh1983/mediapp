# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.core.mail import send_mail

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .models import OTP
from .serializers import OTPSerializer
from helper.utils import is_valid_mobile
import authentication


class GenerateOTPViewSet(ViewSet):
    """View to generate OTP"""

    @transaction.atomic
    def create(self, request):
        request_data = request.data.copy()
        mobile = str(request_data.get("mobile"))
        email = str(request_data.get("email"))
        no_otp_for_registered_user = request_data.get("no_otp_for_registered_user", False)

        if is_valid_mobile(mobile):
            if no_otp_for_registered_user and OTP.is_mobile_registered(mobile):
                # if mobile is already verified then no need to send OTP and verify OTP
                return Response(
                    data={'mobile': mobile, 'is_verified': True},
                    status=status.HTTP_200_OK)
            else:
                # capture mobile number in our database for first time.
                otp_created = OTP.create_new(mobile)
                send_mail("OTP generated for mobile " + mobile,
                          "OTP: {} generated for your mobile no. {}. This OTP will expire in 2 mins.\n"
                          "Please do not share this otp with anyone else.".format(
                              otp_created.token, mobile),
                          settings.EMAIL_HOST_USER,
                          [settings.EMAIL_HOST_USER, email])
                return Response(
                    data=OTPSerializer(otp_created).data,
                    status=status.HTTP_201_CREATED)  # HTTP code 201 for newly created record
        else:
            return Response(data={'error': 'Invalid mobile number Or invalid email address'},
                            status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPViewSet(ViewSet):
    """View to validate OTP token"""

    @transaction.atomic
    def create(self, request):
        """Verfiy OTP entered by user"""
        request_data = request.data.copy()

        mobile = str(request_data.get("mobile"))  # string
        token = request_data.get("otp")  # integer

        if is_valid_mobile(mobile) and token:
            token = int(token)
            is_verified, error = OTP.verify_token(mobile, token)
            if error:
                return_dict, _status = {'success': False,
                                        'verified': is_verified,
                                        'error': error}, status.HTTP_400_BAD_REQUEST
            else:
                if not request.user.is_otp_verified:
                    _user = authentication.models.AppUserModel.objects.get(id=request.user.id)
                    _user.is_otp_verified = True
                    _user.save()
                return_dict, _status = {'success': True, 'verified': is_verified}, status.HTTP_200_OK

            return Response(data=return_dict, status=_status)
        else:
            return Response(data={'success': False, 'error': 'Invalid mobile number or invalid OTP'},
                            status=status.HTTP_400_BAD_REQUEST)
