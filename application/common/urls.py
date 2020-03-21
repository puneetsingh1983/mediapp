# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import (CountryViewSet, StateViewSet, AddressViewSet,
                    BloodGroupViewSet, QualificationViewSet,
                    ResearchViewSet, LanguageViewSet, SpecializationViewSet,
                    DisciplineViewSet, RegistrationAuthorityViewSet,
                    StaticObjectsView)


router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'state', StateViewSet)
router.register(r'address', AddressViewSet)
# router.register(r'bloodgroup', BloodGroupViewSet)
router.register(r'qualification', QualificationViewSet)
router.register(r'language', LanguageViewSet)
# router.register(r'research', ResearchViewSet)
router.register(r'specialization', SpecializationViewSet)
router.register(r'country', CountryViewSet)
router.register(r'discipline', DisciplineViewSet)
router.register(r'reqisteration-authority', RegistrationAuthorityViewSet)


urlpatterns = [
    url(r'^api/v1/common/', include(router.urls)),
    url(r'^api/v1/common/staticobjects/', StaticObjectsView.as_view())
]