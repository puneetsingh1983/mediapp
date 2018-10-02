# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import OTP


# Register your models here.
@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    pass
