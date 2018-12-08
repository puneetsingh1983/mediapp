# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import (
    DoctorProfile, HealthworkerProfile, Availability, PatientProfile, MedicalRepresentative, TestModelBase64)
from .serializers import (
    DoctorProfileSerializer, HealthworkerProfileSerializer,
    AvailabilitySerializer, PatientProfileSerializer, MRProfileSerializer, TestModelBase64Serializer)
from .filters import DoctorFilter, HealthworkerFilter, PatientFilter
from common.models import Address
from helper.file_handler import decode_base64
from authentication.models import AppUserModel as UserModel
from .utils import validate_n_get



# views
class DoctorProfileViewSet(ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    filter_class = DoctorFilter

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data

        certificate = request_data.get('registration_certificate')
        request_data['registration_certificate'] = decode_base64(certificate)

        profile_pic = request_data.get('profile_pic')
        request_data['profile_pic'] = decode_base64(profile_pic)

        try:
            request_data['address'] = Address.objects.get(id=request_data['address'])
            request_data['user'] = UserModel.objects.get(id=request_data['user'])

        except Address.DoesNotExist:
            Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)
        except UserModel.DoesNotExist:
            Response(data={'error': 'Please provide valid user'}, status=status.HTTP_400_BAD_REQUEST)


        qualifications = validate_n_get(
            class_name='Qualification', records_ids=request_data.pop("qualification"))
        specializations = validate_n_get(
            class_name='Specialization', records_ids=request_data.pop("specialization"))
        researches = validate_n_get(
            class_name='Research', records_ids=request_data.pop("research"))
        associated_with = validate_n_get(
            class_name='Organization', records_ids=request_data.pop("associated_with"))
        languages_can_speak = validate_n_get(
            class_name='Language', records_ids=request_data.pop("languages_can_speak"))
        
        # doctor_profile = DoctorProfile.objects.create(**request_data)
        doctor_profile = DoctorProfile(**request_data)
        doctor_profile.save()

        qualifications and doctor_profile.qualification.add(*qualifications)
        specializations and doctor_profile.specialization.add(*specializations)
        researches and doctor_profile.research.add(*researches)
        associated_with and doctor_profile.associated_with.add(*associated_with)
        languages_can_speak and doctor_profile.languages_can_speak.add(*languages_can_speak)
        
        return Response(data={'success': True}, status=status.HTTP_201_CREATED)



class HealthworkerProfileViewSet(ModelViewSet):
    queryset = HealthworkerProfile.objects.all()
    serializer_class = HealthworkerProfileSerializer
    filter_class = HealthworkerFilter


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    filter_class = PatientFilter


class MRProfileViewSet(ModelViewSet):
    queryset = MedicalRepresentative.objects.all()
    serializer_class = MRProfileSerializer
    # filter_class = PatientFilter


class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class TestModelBase64ViewSet(ModelViewSet):
    queryset = TestModelBase64.objects.all()
    serializer_class = TestModelBase64Serializer

    def create(self, request, *args, **kwargs):
        request_data = request.data
        file_name, file_field = decode_base64(request_data)
        # tmb = TestModelBase64(profile_pic=file_field, name="Testfile.txt")
        # tmb.save()
        serialzeinfo = {'profile_pic': file_field, 'name': file_name}
        serializer_ = TestModelBase64Serializer(data=serialzeinfo)
        serializer_.is_valid()
        import pdb; pdb.set_trace()
        serializer_.save()
        print file_field