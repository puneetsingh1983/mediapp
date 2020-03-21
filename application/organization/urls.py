# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import OrganizationViewSet, OrganizationTypeViewSet


router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'organization-type', OrganizationTypeViewSet)

urlpatterns = [
    url(r'^api/v1/organization/', include(router.urls)),
]