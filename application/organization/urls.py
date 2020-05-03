# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import OrganizationViewSet, OrganizationTypeViewSet, PathologyViewSet


router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
# router.register(r'organization-type', OrganizationTypeViewSet)
router.register(r'pathology', PathologyViewSet)

urlpatterns = [
    url(r'^api/v1/organization/', include(router.urls)),
]