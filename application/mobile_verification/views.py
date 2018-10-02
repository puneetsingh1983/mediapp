# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import OTP
from .serializers import OTPSerializer
from commons.utils import is_valid_mobile


class GenerateOTPViewSet(ViewSet):
    """View to generate OTP"""

    @transaction.atomic
    def create(self, request):
        request_data = request.data
        mobile = str(request_data.get("mobile"))
        if is_valid_mobile(mobile):
            otp_created = OTP.create_new(mobile)
            return Response(data=OTPSerializer(otp_created).data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'error': 'Invalid mobile number'})


class VerifyOTPViewSet(ViewSet):
    """View to validate OTP token"""

    @transaction.atomic
    def create(self, request):
        request_data = request.data
        mobile = str(request_data.get("mobile"))  # string
        token = int(request_data.get("otp"))  # integer

        if is_valid_mobile(mobile):
            is_verified = OTP.verify_token(mobile, token)
            return Response(data={'verified': is_verified}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid mobile number'})
