# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import (Country, State, Qualification,
                     Language, Specialization, Research,
                     BloodGroup, Address, Discipline)
from .serializers import (CountrySerializer, StateSerializer,
                          QualificationSerializer, LanguageSerializer,
                          SpecializationSerializer, ResearchSerializer,
                          BloodGroupSerializer, AddressSerializer, DisciplineSerializer)


# Create your views here.
class CountryViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)


class StateViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (IsAuthenticated,)


class QualificationViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = (IsAuthenticated,)


class LanguageViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)


class SpecializationViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = (IsAuthenticated,)


class ResearchViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = (IsAuthenticated,)


class BloodGroupViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = BloodGroup.objects.all()
    serializer_class = BloodGroupSerializer
    permission_classes = (IsAuthenticated,)


class AddressViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)


class DisciplineViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (IsAuthenticated,)
