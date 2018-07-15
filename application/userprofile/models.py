# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.db import models

from utility.models import BaseModel, Address, Qualification, Specialization, Research, Language, BloodGroup
from organization.models import Organization
from authentication.models import AppUserModel


GENDER = (('-', ' -- '),
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'))


# Profiles
class DoctorProfile(BaseModel):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address)
    registration_number = models.CharField(max_length=25)
    years_of_experience = models.IntegerField()
    qualification = models.ManyToManyField(Qualification)
    specialization = models.ManyToManyField(Specialization)
    Research = models.ManyToManyField(Research)
    associated_with = models.ManyToManyField(Organization, null=True, blank=True)
    languages_can_speak = models.ManyToManyField(Language)
    resume = models.FileField(upload_to='documents/doctor/', null=True, blank=True)
    # medical_registration_certificate
    registration_certificate = models.FileField(upload_to='documents/doctor/')
    user_id = models.ForeignKey(AppUserModel)
    profile_pic = models.FileField(upload_to='documents/doctor/', null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def __str__(self):
        return self.name


class PatientProfile(BaseModel):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address)
    case_summary = models.TextField(null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroup)
    weight = models.PositiveIntegerField(help_text="in Kilogram")
    height = models.PositiveIntegerField(help_text="in Centimeters")
    aadhaar_no = models.PositiveIntegerField()
    alternate_mobile_no = models.PositiveIntegerField(null=True, blank=True)
    user_id = models.ForeignKey(AppUserModel)
    profile_pic = models.FileField(upload_to='documents/patient/')

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def __str__(self):
        self.name


class HealthworkerProfile(BaseModel):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address)
    registration_number = models.CharField(max_length=25)
    years_of_experience = models.IntegerField()
    qualification = models.ManyToManyField(Qualification)
    associated_with = models.ManyToManyField(Organization)
    languages_can_speak = models.ManyToManyField(Language)
    resume = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)
    #medical_registration_certificate
    registration_certificate = models.FileField(upload_to='documents/healthworker/')
    user_id = models.ForeignKey(AppUserModel)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    profile_pic = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def __str__(self):
        self.name


class MedicalRepresentative(BaseModel):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address)
    qualification = models.ManyToManyField(Qualification)
    associated_with = models.ManyToManyField(Organization)
    registration_certificate = models.FileField(upload_to='documents/medicalrepresentative/')
    user_id = models.ForeignKey(AppUserModel)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    profile_pic = models.FileField(upload_to='documents/medicalrepresentative/', null=True, blank=True)

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def __str__(self):
        self.name


class Availability(BaseModel):
    place = models.ForeignKey(Organization)
    date_on = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(DoctorProfile, null=True, blank=True)
    healthworker = models.ForeignKey(HealthworkerProfile, null=True, blank=True)

    def __str__(self):
        self.place.name + " " + self.date_on + self.start_time
