# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import (
    DoctorProfileViewSet, HealthworkerProfileViewSet,
    PatientProfileViewSet, MRProfileViewSet, AvailabilityAPIView,
    UploadProfileDocuements, TestModelBase64ViewSet)
from django.conf import settings


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
    url(r'^api/{}/profile/'.format(settings.API_VERSION,), include(router.urls)),
    url(r'^api/{}/availability/'.format(settings.API_VERSION,), AvailabilityAPIView.as_view()),
    url(r'api/{}/uploadprofiledocs/'.format(settings.API_VERSION,), UploadProfileDocuements.as_view())
]