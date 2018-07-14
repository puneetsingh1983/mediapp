# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utility.models import BaseModel, Qualification, Address

# Create your models here.
class OrganizationType(models.Model):
    text = models.CharField(max_length=100, unique=True)


class Organization(BaseModel):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address)
    contact_number = models.IntegerField(max_length=10)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField()
    associated_company = models.ForeignKey('self', null=True, blank=True)
    gst_no = models.CharField(max_length=15)
    license_no = models.CharField(max_length=25)
    head_of_department = models.CharField(max_length=50)
    qualifications = models.ManyToManyField(Qualification)
    license_doc = models.FileField(upload_to='documents/org/%Y/%M/%D/')
    org_type = models.ForeignKey(OrganizationType)
