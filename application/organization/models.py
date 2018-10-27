# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.models import BaseModel, Qualification, Address
from helper.validators import mobile_validator


# Create your models here.
class OrganizationType(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text


class Organization(BaseModel):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address)
    contact_no = models.CharField(max_length=10, validators=[mobile_validator])
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    associated_company = models.ForeignKey('self', null=True, blank=True)
    gst_no = models.CharField(max_length=15)
    license_no = models.CharField(max_length=25)
    head_of_department = models.CharField(max_length=50, null=True, blank=True)
    qualifications = models.ManyToManyField(Qualification)
    license_doc = models.FileField(upload_to='documents/org/%Y/%m/%d/')
    org_type = models.ForeignKey(OrganizationType)

    def __str__(self):
        return self.name
