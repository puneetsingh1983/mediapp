# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Qualification, Research, BloodGroup, State, Country,
    Specialization, Address, Language, Discipline, RegistrationAuthority,
    Accreditation, Disease, Surgery, Allergy, Immunization, Lifestyle,
    HealthWorkerRegistrationAuthority, AlcoholAddiction, Injury, PathlogyLabType)

# Register your models here.
@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    pass


@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class ResearchAdmin(admin.ModelAdmin):
    pass


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(RegistrationAuthority)
class RegistrationAuthorityAdmin(admin.ModelAdmin):
    pass


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    pass


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    pass


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    pass


@admin.register(Immunization)
class ImmunizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    pass


@admin.register(HealthWorkerRegistrationAuthority)
class HealthWorkerRegistrationAuthorityAdmin(admin.ModelAdmin):
    pass


@admin.register(AlcoholAddiction)
class AlcoholAddictionAuthorityAdmin(admin.ModelAdmin):
    pass


@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    pass


@admin.register(PathlogyLabType)
class PathlogyLabTypeAdmin(admin.ModelAdmin):
    pass
