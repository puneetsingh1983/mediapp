# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Qualification, Research, BloodGroup, State, Country, Specialization, Address, Language)

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
