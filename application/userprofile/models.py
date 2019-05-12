# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import FileExtensionValidator

from common.models import (BaseProfileModel, BaseModel, Qualification,
                           Specialization, Research, Language, BloodGroup,
                           State, Discipline, RegistrationAuthority)
from organization.models import Organization
from helper.validators import mobile_validator


MODE_1 = 'online'
MODE_2 = 'offline'
MODE_3 = 'out_door'

AVAILABILITY_MODE = ((MODE_1, 'Online'),
                     (MODE_2, 'Offline'),
                     (MODE_3, 'Out Door'))


# Profiles
class DoctorProfile(BaseProfileModel):
    registration_number = models.CharField(max_length=25, unique=True)
    years_of_experience = models.IntegerField()
    qualification = models.ManyToManyField(Qualification, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    achievement_research = models.TextField(null=True, blank=True,
                                            help_text="Achievements and researches")
    associated_with = models.ManyToManyField(Organization, blank=True)
    languages_can_speak = models.ManyToManyField(Language, blank=True)
    resume = models.FileField(upload_to='documents/doctor/', null=True, blank=True)
                              # validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
    # medical_registration_certificate
    authority_registered_with = models.ForeignKey(RegistrationAuthority, null=True, blank=True)
    registration_certificate = models.FileField(upload_to='documents/doctor/')
    profile_pic = models.FileField(upload_to='documents/doctor/', null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    discipline = models.ManyToManyField(Discipline, blank=True)

    def __str__(self):
        return self.name


class PatientProfile(BaseProfileModel):
    # TODO- handling for multiple prescription and test reports
    case_summary = models.TextField(null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroup, null=True, blank=True, on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(help_text="in Kilogram", null=True, blank=True)
    height = models.PositiveIntegerField(help_text="in Centimeters", null=True, blank=True)
    aadhaar_no = models.PositiveIntegerField(null=True, blank=True)
    alternate_mobile_no = models.PositiveIntegerField(null=True, blank=True)
    profile_pic = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)
    languages_can_speak = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.name


class HealthworkerProfile(BaseProfileModel):
    registration_number = models.CharField(max_length=25)
    years_of_experience = models.IntegerField(null=True, blank=True)
    qualification = models.ManyToManyField(Qualification, blank=True)
    associated_with = models.ManyToManyField(Organization, blank=True)
    languages_can_speak = models.ManyToManyField(Language, blank=True)
    resume = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)
    #medical_registration_certificate
    registration_certificate = models.FileField(upload_to='documents/healthworker/')
    profile_pic = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)

    def __str__(self):
        return self.name


class MedicalRepresentative(BaseProfileModel):
    qualification = models.ManyToManyField(Qualification, blank=True)
    associated_with = models.ManyToManyField(Organization, blank=True)
    registration_certificate = models.FileField(upload_to='documents/medicalrepresentative/')
    profile_pic = models.FileField(upload_to='documents/medicalrepresentative/', null=True, blank=True)
    languages_can_speak = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.name


class Availability(BaseModel):
    """Model to capture person's availability - Online, Offline or Outdoor"""

    availability_mode = models.CharField(max_length=9, choices=AVAILABILITY_MODE, default=1)
    # Place where person will be available physically (Offline)
    venue = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.PROTECT)
    # Day and time
    start_time = models.TimeField()
    end_time = models.TimeField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    # online
    online_chat = models.NullBooleanField()
    online_video_call = models.NullBooleanField()
    online_voice_call = models.NullBooleanField()

    # outdoor
    outdoor_travel_upto = models.PositiveIntegerField(null=True, blank=True)
    outdoor_travel_city = models.CharField(max_length=50, null=True, blank=True)
    outdoor_travel_state = models.ForeignKey(State, null=True, blank=True)
    outdoor_travel_locality = models.CharField(max_length=50, null=True, blank=True)

    # contact number based on place/mode
    contact_no = models.CharField(max_length=10, validators=[mobile_validator])

    doctor = models.ForeignKey(DoctorProfile, null=True, blank=True, on_delete=models.PROTECT)
    health_worker = models.ForeignKey(HealthworkerProfile, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)


class TestModelBase64(models.Model):
    profile_pic = models.FileField(upload_to='documents/testing/', null=True, blank=True)
    name = models.CharField(max_length=10, null=True, blank=True)

