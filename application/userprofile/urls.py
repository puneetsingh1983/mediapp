# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import (
    DoctorProfileViewSet, HealthworkerProfileViewSet, PatientProfileViewSet, AvailabilityViewSet)


router = routers.DefaultRouter()
router.register(r'doctor', DoctorProfileViewSet)
router.register(r'healthworker', HealthworkerProfileViewSet)
router.register(r'patient', PatientProfileViewSet)
router.register(r'availability', AvailabilityViewSet)

urlpatterns = [
    url(r'^api/v1/profile/', include(router.urls)),
]