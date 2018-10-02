# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utility.models import BaseModel
from commons.totp_generate_verify import TOTPVerification
from commons.validators import mobile_validator


class OTP(BaseModel):
    """Model to capture mobile, generated OTP and verification status"""
    mobile = models.CharField(max_length=10, validators=[mobile_validator])
    token = models.PositiveIntegerField(max_length=6, null=True, blank=True)
    verified = models.BooleanField(default=False)

    @classmethod
    def verify_token(cls, mobile, token):
        """validate given token and update verified flag for given mobile"""

        is_valid = TOTPVerification().verify_token(token)
        try:
            # get un-verified mobile token and update flag
            obj = cls.objects.get(mobile=mobile, token=token, verified=False)
            obj.verified = is_valid
            obj.save()
        except OTP.DoesNotExist:
            print ("No record found for mobile no. {}".format(mobile,))
            is_valid = False

        return is_valid

    @classmethod
    def create_new(cls, mobile):
        obj = OTP(
            mobile=mobile,
            token=TOTPVerification().generate_token(),
            verified=False)
        obj.save()
        return obj

    def __str__(self):
        return "{} - {}".format(self.mobile, self.token)
