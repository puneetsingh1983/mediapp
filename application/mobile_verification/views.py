# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.core.mail import send_mail

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import OTP
from .serializers import OTPSerializer
from commons.utils import is_valid_mobile
from django.conf import settings


class GenerateOTPViewSet(ViewSet):
    """View to generate OTP"""

    @transaction.atomic
    def create(self, request):
        request_data = request.data
        mobile = str(request_data.get("mobile"))
        if is_valid_mobile(mobile):
            if OTP.is_mobile_registered(mobile):
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
                          [settings.EMAIL_HOST_USER, ])
                return Response(
                    data=OTPSerializer(otp_created).data,
                    status=status.HTTP_201_CREATED)  # HTTP code 201 for newly created record
        else:
            return Response(data={'error': 'Invalid mobile number'})


class VerifyOTPViewSet(ViewSet):
    """View to validate OTP token"""

    @transaction.atomic
    def create(self, request):
        """Verfiy OTP entered by user"""
        request_data = request.data
        mobile = str(request_data.get("mobile"))  # string
        token = int(request_data.get("otp"))  # integer

        if is_valid_mobile(mobile):
            is_verified = OTP.verify_token(mobile, token)
            return Response(data={'verified': is_verified}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid mobile number'})
