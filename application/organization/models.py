# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.models import (BaseModel, Specialization, Address,
                           Accreditation, PathlogyLabType)
from helper.validators import mobile_validator


# Create your models here.
class OrganizationType(models.Model):
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text


class Organization(BaseModel):
    """Organization Model. Ex- Hospital, Clinic, Digital Clinic or Pharmacy or Medical Store"""
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    mobile_no = models.CharField(max_length=10, validators=[mobile_validator])
    landline_no = models.CharField(max_length=11, null=True, blank=True,
                                   help_text="Stored as <STD-PHONE_NO>. Ex- '011-32323234' or '07582-676123'")
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    associated_company = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    gst_no = models.CharField(max_length=15, null=True, blank=True)
    license_no = models.CharField(max_length=25, null=True, blank=True,
                                  help_text="Required for hospitals/clinics/medical-stores")
    head_of_department = models.CharField(max_length=50, null=True, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    license_doc = models.FileField(upload_to='documents/org/%Y/%m/%d/', null=True, blank=True)
    org_type = models.ForeignKey(OrganizationType, on_delete=models.PROTECT)
    accreditation = models.ForeignKey(Accreditation, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_records(cls, id_list):
        return cls.objects.filter(id__in=id_list)

    def save(self, *args, **kwargs):
        if self.org_type.text.lower() == 'hospital':
            if not self.gst_no:
                raise ValueError("GST No not provided!")
            if not self.license_no:
                raise ValueError("License No not provided!")

        super(Organization, self).save(*args, **kwargs)


class Pathology(BaseModel):
    """Organization Model. Ex- Hospital, Clinic, Digital Clinic or Pharmacy or Medical Store"""
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    lab_type = models.ForeignKey(PathlogyLabType, on_delete=models.PROTECT, related_name="pathalogies")
    mobile_no = models.CharField(max_length=10, validators=[mobile_validator])
    landline_no = models.CharField(max_length=11, null=True, blank=True,
                                   help_text="Stored as <STD-PHONE_NO>. Ex- '011-32323234' or '07582-676123'")
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    date_of_establishment = models.DateField(max_length=8, null=True, blank=True)
    accreditation_year = models.PositiveIntegerField(max_length=4, null=True, blank=True)
    accreditation = models.ForeignKey(Accreditation, on_delete=models.PROTECT, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    associated_company = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    gst_no = models.CharField(max_length=15, null=True, blank=True)
    license_no = models.CharField(max_length=25, null=True, blank=True,
                                  help_text="Required for hospitals/clinics/medical-stores")
    head_of_lab = models.CharField(max_length=50, null=True, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    license_doc = models.FileField(upload_to='documents/Pathology/%Y/%m/%d/', null=True, blank=True)


    def __str__(self):
        return self.name

    @classmethod
    def get_records(cls, id_list):
        return cls.objects.filter(id__in=id_list)

