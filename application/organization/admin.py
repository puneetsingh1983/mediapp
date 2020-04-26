# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (Organization, OrganizationType, Pathalogy)


# Register your models here.
@admin.register(Organization)
class OrganizationeAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Pathalogy)
class PathalogyAdmin(admin.ModelAdmin):
    pass

