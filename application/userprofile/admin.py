# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import (DoctorProfile, HealthworkerProfile, PatientProfile, MedicalRepresentative,
                     OfflineAvailability, OnlineAvailability, OutdoorAvailability,
                     AvailabilitySchedule, MasterConsultationFeeDiscountDetails)


# Register your models here.
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(HealthworkerProfile)
class HealthworkerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(OfflineAvailability)
class OfflineAvailabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalRepresentative)
class MRProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(OnlineAvailability)
class OnlineAvailabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(OutdoorAvailability)
class OutdoorAvailabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(AvailabilitySchedule)
class AvailabilityScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(MasterConsultationFeeDiscountDetails)
class MasterConsultationFeeDiscountDetails(admin.ModelAdmin):
    pass
