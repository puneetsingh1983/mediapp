# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import (
    DoctorProfileViewSet, HealthworkerProfileViewSet,
    PatientProfileViewSet, MRProfileViewSet, AvailabilityAPIView, TestModelBase64ViewSet)


router = routers.DefaultRouter()
router.register(r'doctor', DoctorProfileViewSet)
router.register(r'healthworker', HealthworkerProfileViewSet)
router.register(r'patient', PatientProfileViewSet)
router.register(r'medrep', MRProfileViewSet)
router.register(r'testModelBase64', TestModelBase64ViewSet)

# router1 = routers.DefaultRouter()
# router1.register(r'online', OnlineAvailabilityAPIView)
# router1.register(r'offline', OfflineAvailabilityAPIView)
# router1.register(r'outdoor', OutdoorAvailabilityAPIView)

urlpatterns = [
    url(r'^api/v1/profile/', include(router.urls)),
    url(r'^api/v1/availability/', AvailabilityAPIView.as_view()),
]