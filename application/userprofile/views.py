# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from .models import (
    DoctorProfile, HealthworkerProfile, Availability, PatientProfile)
from .serializers import (
    DoctorProfileSerializer, HealthworkerProfileSerializer, AvailabilitySerializer, PatientProfileSerializer)
from .filters import DoctorFilter, HealthworkerFilter, PatientFilter


# views
class DoctorProfileViewSet(ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    filter_class = DoctorFilter

    def create(self, request, *args, **kwargs):
        request_data = request.data

        _certificate = request_data.get('registration_certificate')


class HealthworkerProfileViewSet(ModelViewSet):
    queryset = HealthworkerProfile.objects.all()
    serializer_class = HealthworkerProfileSerializer
    filter_class = HealthworkerFilter


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    filter_class = PatientFilter


class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
