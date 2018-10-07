# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import GenerateOTPViewSet, VerifyOTPViewSet


router = routers.DefaultRouter()
router.register(r'generate-otp', GenerateOTPViewSet, base_name='generate-otp')
router.register(r'verify-otp', VerifyOTPViewSet, base_name='verify-otp')

urlpatterns = [
    url(r'^api/v1/mobile/', include(router.urls)),
]