# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .constants import ID_CARD_TYPE, RELATIONSHIP

from .models import (Country, State, Qualification, Accreditation,
                     Language, Specialization, Research,
                     BloodGroup, Address, Discipline, RegistrationAuthority,
                     Disease, Surgery, Allergy, Immunization, Lifestyle,
                     AlcoholAddiction, Injury)
from .serializers import (CountrySerializer, StateSerializer, AccreditationSerializer,
                          QualificationSerializer, LanguageSerializer,
                          SpecializationSerializer, ResearchSerializer,
                          BloodGroupSerializer, AddressSerializer, DisciplineSerializer,
                          RegistrationAuthoritySerializer, DiseaseSerializer,
                          SurgerySerializer, AllergySerializer, ImmunizationSerializer,
                          LifestyleSerializer, AlcoholAddictionSerializer, InjurySerializer)
from organization.models import OrganizationType
from organization.serializers import OrganizationTypeSerializer


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


class RegistrationAuthorityViewSet(ModelViewSet):
    # TODO: Need to implement role or user based permission so that one can't view other's data

    queryset = RegistrationAuthority.objects.all()
    serializer_class = RegistrationAuthoritySerializer
    permission_classes = (IsAuthenticated,)


class StaticObjectsView(APIView):
    def get(self, request, format=None):
        registeration_auths = RegistrationAuthoritySerializer(
            RegistrationAuthority.objects.all(), many=True)
        disciplines = DisciplineSerializer(
            Discipline.objects.all(), many=True)
        specializations = SpecializationSerializer(
            Specialization.objects.all(), many=True)
        bloodGroups = BloodGroupSerializer(
            BloodGroup.objects.all(), many=True)
        languages = LanguageSerializer(
            Language.objects.all(), many=True)
        qualifications = QualificationSerializer(
            Qualification.objects.all(), many=True)
        states = StateSerializer(
            State.objects.all(), many=True)
        countries = CountrySerializer(
            Country.objects.all(), many=True)
        organization_type = OrganizationTypeSerializer(
            OrganizationType.objects.all(), many=True)
        accreditation = AccreditationSerializer(
            Accreditation.objects.all(), many=True)
        disease = DiseaseSerializer(Disease.objects.all(), many=True)
        surgery = SurgerySerializer(Surgery.objects.all(), many=True)
        allergy = AllergySerializer(Allergy.objects.all(), many=True)
        immuization = ImmunizationSerializer(Immunization.objects.all(), many=True)
        lifestyle = LifestyleSerializer(Lifestyle.objects.all(), many=True)
        alcohol_addiction = AlcoholAddictionSerializer(AlcoholAddiction.objects.all(), many=True)
        injury = InjurySerializer(Injury.objects.all(), many=True)
        research = ResearchSerializer(Research.objects.all(), many=True)
        id_card_type = [dict(id=x[0], text=x[1]) for x in ID_CARD_TYPE if x[0]]
        relationships = [dict(id=x[0], text=x[1]) for x in RELATIONSHIP if x[0]]

        return Response(data={'registered_authority': registeration_auths.data,
                              'discipline': disciplines.data,
                              'specialization': specializations.data,
                              'bloodGroup': bloodGroups.data,
                              'language': languages.data,
                              'qualification': qualifications.data,
                              'state': states.data,
                              'country': countries.data,
                              'org_type': organization_type.data,
                              'accreditation': accreditation.data,
                              'research': research.data,
                              'disease': disease.data,
                              'surgery': surgery.data,
                              'allergy': allergy.data,
                              'immuization': immuization.data,
                              'lifestyle': lifestyle.data,
                              'alcohol_addiction': alcohol_addiction.data,
                              'injury': injury.data,
                              'id_card_type': id_card_type,
                              'relationships': relationships
                              }, status=status.HTTP_200_OK)
