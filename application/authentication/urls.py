# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import AppUserViewSet


router = routers.DefaultRouter()
router.register(r'user', AppUserViewSet)

urlpatterns = [
    url(r'^api/v1/authentication/', include(router.urls)),
]