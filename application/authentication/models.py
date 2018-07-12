# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.core.validators import RegexValidator


USER_STATUSES = ((1, 'Approval PENDING'),
                 (2, 'Approved'),
                 (3, 'Rejected'),
                 (4, 'On Hold'))

USER_TYPE = ((1, 'Doctor'),
             (2, 'Health Worker'),
             (3, 'Patient'),
             (4, 'Medical Representative'),
             (5, 'Others'))


# User model manager
class AppUserManager(BaseUserManager):
    def _valdiate(self, email, mobile):
        if not email:
            raise ValueError("User must have email address")
        if not mobile:
            raise ValueError("User must have mobile number")

    def create_user(self,email, mobile, user_type, user_status, password=None, **kwargs):
        self._valdiate(email, mobile)
        user = self.model(email=self.normalize_email(email),
                          mobile=mobile, user_type=user_type or USER_TYPE[-1][0],
                          user_status=user_status or USER_STATUSES[0][0])
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, mobile, user_type=None, user_status=None,
                         password=None):
        self._valdiate(email, mobile)
        user = self.model(email=self.normalize_email(email),
                          mobile=mobile, user_type=user_type or USER_TYPE[0][-1],
                          user_status=user_status or USER_STATUSES[0][0],)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


# User model
class AppUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email Address", unique=True)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex="^\d{10}$",
                                   message="Mobile number must have 10 digits",
                                   code="invalid_mobile")],
        unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=1)
    user_status = models.IntegerField(choices=USER_STATUSES, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    modifile_on = models.DateTimeField(auto_now=True)
    reason_for_modification = models.TextField(null=True, blank=True)
    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile',]

    class Meta:
        verbose_name = "application User"
        verbose_name_plural = "Appication Users"
        ordering = ('id',)

    def modify_user(self):
        pass

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff
