# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import (
    DoctorProfileViewSet, HealthworkerProfileViewSet, PatientProfileViewSet, AvailabilityView,
    OfflineAvailabilityViewSet, OnlineAvailabilityViewSet, OutdoorAvailabilityViewSet,
    MRProfileViewSet, TestModelBase64ViewSet)


router = routers.DefaultRouter()
router.register(r'doctor', DoctorProfileViewSet)
router.register(r'healthworker', HealthworkerProfileViewSet)
router.register(r'patient', PatientProfileViewSet)
router.register(r'medrep', MRProfileViewSet)
router.register(r'onlineavailability', OnlineAvailabilityViewSet)
router.register(r'offlineavailability', OfflineAvailabilityViewSet)
router.register(r'outdooravailability', OutdoorAvailabilityViewSet)
router.register(r'testModelBase64', TestModelBase64ViewSet)

urlpatterns = [
    url(r'^api/v1/profile/', include(router.urls)),
    url(r'^api/v1/availability/', AvailabilityView.as_view())
]