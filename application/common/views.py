# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
rom rest_framework.permissions import AllowAny

from .models import (Country, State, Qualification,
                     Language, Specialization, Research,
                     BloodGroup)
from .serializers import CountrySerializer


# Create your views here.
class CountryViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)