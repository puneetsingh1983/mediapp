# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUserModel


class AppUserAdmin(UserAdmin):
    list_display = ('email', 'mobile', 'user_type', 'user_status')
    ordering = ('email', 'mobile')

# Register your models here.
admin.site.register(AppUserModel, AppUserAdmin)
