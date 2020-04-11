# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import GenerateOTPViewSet, VerifyOTPViewSet


router = routers.DefaultRouter()
router.register(r'generate-otp', GenerateOTPViewSet, basename='generate-otp')
router.register(r'verify-otp', VerifyOTPViewSet, basename='verify-otp')

urlpatterns = [
    url(r'^api/v1/mobile/', include(router.urls)),
]