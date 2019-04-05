# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail

from common.models import BaseModel
from helper.totp_generate_verify import TOTPVerification
from helper.validators import mobile_validator
from django.conf import settings


class OTP(BaseModel):
    """Model to capture mobile, generated OTP and verification status"""
    mobile = models.CharField(max_length=10, validators=[mobile_validator])
    token = models.PositiveIntegerField(null=True, blank=True)  # OTP
    verified = models.BooleanField(default=False)

    @classmethod
    def verify_token(cls, mobile, token):
        """validate given token and update verified flag for given mobile"""

        is_valid = TOTPVerification().verify_token(token)
        error = ''
        if is_valid:
            try:
                # get un-verified mobile token and update flag
                obj = cls.objects.get(mobile=mobile, token=token, verified=False)
                obj.verified = is_valid  # TODO: as of now setting it to true because TOTP verification is not working in Amazon machine deployment
                obj.save()
            except OTP.DoesNotExist:
                print ("No record found for mobile no. {}".format(mobile,))
                is_valid, error = False, "Either mobile number or OTP is not correct."
            return is_valid, error
        else:
            return False, "Either mobile number or OTP is not correct."

    @classmethod
    def create_new(cls, mobile):
        """generate OTP for given mobile"""
        obj = OTP(
            mobile=mobile,
            token=TOTPVerification().generate_token(),
            verified=False)
        obj.save()
        return obj

    @classmethod
    def create_new_send(cls, mobile, email=None):
        """generate OTP and send it to given mobile and email"""
        obj = OTP(
            mobile=mobile,
            token=TOTPVerification().generate_token(),
            verified=False)
        obj.save()

        # TODO- send OTP in SMS to given mobile

        if email:
            # Send OTP in email
            send_mail("OTP generated for mobile " + mobile,
                      "OTP: {} generated for your mobile no. {}. This OTP will expire in 2 mins.\n"
                      "Please do not share this otp with anyone else.".format(
                          obj.token, mobile),
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_HOST_USER, email])
        return obj

    @classmethod
    def is_mobile_registered(cls, mobile):
        mobile = cls.objects.filter(mobile=mobile)
        return mobile and True or False

    def __str__(self):
        return "{} - {}".format(self.mobile, self.token)
