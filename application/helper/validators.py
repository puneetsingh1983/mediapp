# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from .utils import is_valid_mobile


def mobile_validator(value):
    if not is_valid_mobile(value):
        raise ValidationError("Mobile no. is invalid! Please enter 10 digit mobile number!")


