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
    """Availability: time, Day, contract no, appointment limit, fee and discount"""

    doctor = models.ForeignKey(DoctorProfile, null=True, blank=True, on_delete=models.PROTECT,
                               related_name="%(class)s")

    # Time
    start_time = models.TimeField()
    end_time = models.TimeField()

    # Day
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    appointment_limit = models.PositiveIntegerField(null=True, blank=True)
    contact_no = models.CharField(max_length=10, validators=[mobile_validator])

    class Meta:
        abstract = True


class OfflineAvailability(Availability):
    """Offline availability description"""

    # place where doctor will be available for visit
    venue = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.PROTECT,
                              related_name="offline_availabilities")
    consultation_fee = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True, blank=True)


class OnlineAvailability(Availability):
    """Online availability description"""

    chat = models.BooleanField(default=False)
    video_call = models.BooleanField(default=False)
    voice_call = models.BooleanField(default=False)

    chat_fee = models.PositiveIntegerField()
    video_call_fee = models.PositiveIntegerField()
    voice_call_fee= models.PositiveIntegerField()

    chat_discount = models.PositiveIntegerField(null=True, blank=True)
    video_call_discount = models.PositiveIntegerField(null=True, blank=True)
    voice_call_discount = models.PositiveIntegerField(null=True, blank=True)


class OutdoorAvailability(Availability):
    """Outdoor availability description"""

    outdoor_travel_upto = models.PositiveIntegerField(null=True, blank=True)
    outdoor_travel_city = models.CharField(max_length=50, null=True, blank=True)
    outdoor_travel_state = models.ForeignKey(State, null=True, blank=True, related_name="outdoor_availabilities")
    outdoor_travel_locality = models.CharField(max_length=50, null=True, blank=True)

    fee_0_to_5km = models.PositiveIntegerField(null=True, blank=True)
    fee_5_to_10km = models.PositiveIntegerField(null=True, blank=True)
    fee_10_to_15km = models.PositiveIntegerField(null=True, blank=True)
    fee_15_to_20km = models.PositiveIntegerField(null=True, blank=True)
    fee_above_20km = models.PositiveIntegerField(null=True, blank=True)

    discount_0_to_5km = models.PositiveIntegerField(null=True, blank=True)
    discount_5_to_10km = models.PositiveIntegerField(null=True, blank=True)
    discount_10_to_15km = models.PositiveIntegerField(null=True, blank=True)
    discount_15_to_20km = models.PositiveIntegerField(null=True, blank=True)
    discount_above_20km = models.PositiveIntegerField(null=True, blank=True)


class TestModelBase64(models.Model):
    profile_pic = models.FileField(upload_to='documents/testing/', null=True, blank=True)
    name = models.CharField(max_length=10, null=True, blank=True)

