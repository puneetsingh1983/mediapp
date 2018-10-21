# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUserModel


class AppUserCreationForm(UserCreationForm):
    """
    A form that creates a custom user with no privilages
    form a provided email and password.
    """

    class Meta(UserCreationForm.Meta):
        model = AppUserModel
        fields = '__all__'


class AppUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta(UserChangeForm.Meta):
        model = AppUserModel
        fields = '__all__'


class AppUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'mobile', 'password')}),
        ('Personal info', {'fields': ('user_type', 'user_status')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'mobile', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

    form = AppUserChangeForm
    add_form = AppUserCreationForm

    list_display = ('username', 'mobile', 'user_type', 'user_status')
    ordering = ('username', 'mobile')

    search_fields = ('username', 'mobile')
    exclude = ('first_name', 'last_name')


# Register your models here.
admin.site.register(AppUserModel, AppUserAdmin)
