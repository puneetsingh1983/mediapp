# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from .models import (
    DoctorProfile, HealthworkerProfile, Availability, PatientProfile)
from .serializers import (
    DoctorProfileSerializer, HealthworkerProfileSerializer, AvailabilitySerializer, PatientProfileSerializer)


# views
class DoctorProfileViewSet(ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer


class HealthworkerProfileViewSet(ModelViewSet):
    queryset = HealthworkerProfile.objects.all()
    serializer_class = HealthworkerProfileSerializer


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer


class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
