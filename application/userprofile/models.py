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


AADHAAR_CARD = 'uid'
PASSPORT = 'pp'
DRIVING_LICENSE = 'dl'
VOTER_ID_CARD = 'vid'
PAN_CARD = 'pan'
COMPANY_ID_CARD = 'cid'
ID_CARD_TYPE = (('', ' -- '),
                (AADHAAR_CARD, 'Aadhaar Card (UID)'),
                (PASSPORT, 'Passport'),
                (DRIVING_LICENSE, 'Driving License'),
                (VOTER_ID_CARD, 'Voter ID Card '),
                (PAN_CARD, 'Pan Card'),
                (COMPANY_ID_CARD, 'Company ID Card'),)


# Profiles
class DoctorProfile(BaseProfileModel):
    registration_number = models.CharField(max_length=25, unique=True)
    years_of_experience = models.IntegerField()
    qualification = models.ManyToManyField(Qualification, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    achievement_research = models.TextField(null=True, blank=True,
                                            help_text="Achievements and researches")
    associated_with = models.ManyToManyField(Organization, blank=True)
    # languages_can_speak = models.ManyToManyField(Language, blank=True)
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
    alternate_mobile_no = models.PositiveIntegerField(null=True, blank=True)
    profile_pic = models.FileField(upload_to='documents/patient/', null=True, blank=True)
    # languages_can_speak = models.ManyToManyField(Language, blank=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    identity_card_type = models.CharField(max_length=1, choices=ID_CARD_TYPE, default='')
    identity_card_no = models.CharField(max_length=50, null=True, blank=True)
    referred_by = models.CharField(max_length=70, blank=True, null=True)
    have_mediclaim = models.BooleanField(default=False)
    dob = models.DateField(max_length=8, blank=True, null=True)


    def __str__(self):
        return self.name


class HealthworkerProfile(BaseProfileModel):
    registration_number = models.CharField(max_length=25, unique=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    qualification = models.ManyToManyField(Qualification, blank=True)
    associated_with = models.ManyToManyField(Organization, blank=True)
    # languages_can_speak = models.ManyToManyField(Language, blank=True)
    resume = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)
    #medical_registration_certificate
    registration_certificate = models.FileField(upload_to='documents/healthworker/')
    profile_pic = models.FileField(upload_to='documents/healthworker/', null=True, blank=True)

    def __str__(self):
        return self.name


class MedicalRepresentative(BaseProfileModel):
    registration_number = models.CharField(max_length=25, unique=True)
    qualification = models.ManyToManyField(Qualification, blank=True)
    associated_with = models.ManyToManyField(Organization, blank=True)
    registration_certificate = models.FileField(upload_to='documents/medicalrepresentative/')
    profile_pic = models.FileField(upload_to='documents/medicalrepresentative/', null=True, blank=True)
    # languages_can_speak = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.name


class AvailabilitySchedule(models.Model):
    """AvailabilitySchedule: time, Day.
       Assumption:- re-usability, multiple availabilities can have same schedule
    """
    # Schedule: [{ days: ['mon', 'tue'],
    #             time: {'start': 10:00 AM, 'end': 14:00 PM}}]
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

    def __str__(self):
        return "{}".format(self.id)


class BaseAvailability(BaseModel):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.PROTECT,
                               related_name="doctor_%(class)s")
    schedule = models.ForeignKey(AvailabilitySchedule, on_delete=models.PROTECT,
                               related_name="schedule_%(class)s")
    appointment_limit = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.id)


class OfflineAvailability(BaseAvailability):
    """Offline availability description"""

    # place where doctor will be available for visit
    venue = models.ForeignKey(Organization, on_delete=models.PROTECT,
                              related_name="offline_availabilities")

    # consultation fee details will be different as per clinics and Hospitals
    offline_consultation_fee = models.PositiveIntegerField()
    offline_discount = models.PositiveIntegerField(null=True, blank=True)
    contact_no = models.CharField(max_length=11, validators=[mobile_validator],
                                  help_text="10 digit mobile number or 11 digit landline number")


class OnlineAvailability(BaseAvailability):
    """Online availability description"""

    chat = models.BooleanField(default=False)
    video_call = models.BooleanField(default=False)
    voice_call = models.BooleanField(default=False)


class OutdoorAvailability(BaseAvailability):
    """Outdoor availability description"""

    outdoor_travel_upto = models.PositiveIntegerField(null=True, blank=True)
    outdoor_travel_city = models.CharField(max_length=50, null=True, blank=True)
    outdoor_travel_state = models.ForeignKey(State, null=True, blank=True, related_name="outdoor_availabilities")
    outdoor_travel_locality = models.CharField(max_length=50, null=True, blank=True)


class ConsultationDetails(BaseModel):
    """Default consultation details. Will be appicable if not given specific consultation details"""
    doctor = models.OneToOneField(DoctorProfile, on_delete=models.PROTECT)

    # offline consultation
    offline_consultation_fee = models.PositiveIntegerField(null=True, blank=True)
    offline_discount = models.PositiveIntegerField(null=True, blank=True)
    contact_no_offline_consultation = models.CharField(
        max_length=11, validators=[mobile_validator], null=True, blank=True,
        help_text="10 digit mobile number or 11 digit landline number")

    # online consultation
    contact_no_online_consultation = models.CharField(
        max_length=11, validators=[mobile_validator], null=True, blank=True,
        help_text="10 digit mobile number or 11 digit landline number")
    chat_fee = models.PositiveIntegerField(null=True, blank=True)
    video_call_fee = models.PositiveIntegerField(null=True, blank=True)
    voice_call_fee = models.PositiveIntegerField(null=True, blank=True)

    chat_discount = models.PositiveIntegerField(null=True, blank=True)
    video_call_discount = models.PositiveIntegerField(null=True, blank=True)
    voice_call_discount = models.PositiveIntegerField(null=True, blank=True)

    # outdoor consultation
    contact_no_outdoor_consultation = models.CharField(
        max_length=11, validators=[mobile_validator], null=True, blank=True,
        help_text="10 digit mobile number or 11 digit landline number")
    outdoor_consultation_fee = models.PositiveIntegerField(null=True, blank=True)
    outdoor_discount = models.PositiveIntegerField(null=True, blank=True)
    outdoor_additional_charges = models.PositiveIntegerField(null=True, blank=True)


class TestModelBase64(models.Model):
    profile_pic = models.FileField(upload_to='documents/testing/', null=True, blank=True)
    name = models.CharField(max_length=10, null=True, blank=True)

