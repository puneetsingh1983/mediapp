# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import DoctorProfile, HealthworkerProfile, Availability, PatientProfile, MedicalRepresentative


# Register your models here.
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(HealthworkerProfile)
class HealthworkerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalRepresentative)
class MRProfileAdmin(admin.ModelAdmin):
    pass
