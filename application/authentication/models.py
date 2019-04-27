# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.core.validators import RegexValidator


DEFAULT_TYPE = ''
DOCTOR = 'doctor'
HEALTH_WORKER = 'health_worker'
PATIENT = 'patient'
MED_REP = 'medical_rep'
OTHER = 'other'

PENDING_APPROVAL = 'pending_approval'  # approval pending
APPROVED = 'approved'
REJECTED = 'rejected'
ON_HOLD = 'on_hold'

USER_STATUSES = ((PENDING_APPROVAL, 'Approval Pending'),
                 (APPROVED, 'Approved'),
                 (REJECTED, 'Rejected'),
                 (ON_HOLD, 'On Hold'))

USER_TYPE = ((DEFAULT_TYPE, ' -- '),
             (DOCTOR, 'Doctor'),
             (HEALTH_WORKER, 'Health Worker'),
             (PATIENT, 'Patient'),
             (MED_REP, 'Medical Representative'),
             (OTHER, 'Other'))


# User model manager
class AppUserManager(BaseUserManager):
    """Application user model manager"""
    @staticmethod
    def validate(email, mobile, password):
        if not email:
            raise ValueError("User must have email address")
        if not mobile:
            raise ValueError("User must have mobile number")
        if not password:
            raise ValueError("User must have password")

    def create_user(self, username, mobile, user_type, user_status, password, **kwargs):
        self.validate(username, mobile, password)
        user = self.model(username=self.normalize_email(username),
                          mobile=mobile, user_type=user_type or DEFAULT_TYPE,
                          user_status=user_status or PENDING_APPROVAL)
        user.set_password(password)
        user.full_name = kwargs.get('full_name')

        user.save()
        return user

    def create_superuser(self, username, mobile, password=None, user_type=None,
                         user_status=None):
        self.validate(username, mobile, password)
        user = self.model(username=self.normalize_email(username),
                          mobile=mobile, user_type=user_type or DEFAULT_TYPE,
                          user_status=user_status or PENDING_APPROVAL,)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


# User model
class AppUserModel(AbstractBaseUser, PermissionsMixin):
    """Application use model"""
    username = models.EmailField(verbose_name="Email Address", unique=True)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex="^\d{10}$",
            message="Mobile number must have 10 digits",
            code="invalid_mobile")],
        unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=16, choices=USER_TYPE, default=0)
    user_status = models.CharField(max_length=16, choices=USER_STATUSES, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    reason_for_modification = models.TextField(null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    is_otp_verified = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mobile',]

    class Meta:
        verbose_name = "application User"
        verbose_name_plural = "Appication Users"
        ordering = ('id',)

    def modify_user(self):
        pass

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff

    @property
    def email(self):
        return self.username
