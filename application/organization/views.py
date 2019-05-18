# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from .models import OrganizationType, Organization
from .serializers import OrganizationSerializer, OrganizationTypeSerializer
from .filters import OrganizationFilter


# views
class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_class = OrganizationFilter


class OrganizationTypeViewSet(ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer
