# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    DoctorProfile, HealthworkerProfile, Availability, PatientProfile, MedicalRepresentative, TestModelBase64)
from .serializers import (
    DoctorProfileSerializer, HealthworkerProfileSerializer,
    AvailabilitySerializer, PatientProfileSerializer, MRProfileSerializer, TestModelBase64Serializer)
from .filters import DoctorFilter, HealthworkerFilter, PatientFilter
from common.models import Address, BloodGroup, RegistrationAuthority
from helper.file_handler import decode_base64
from authentication.models import AppUserModel as UserModel
from .utils import validate_n_get, bulk_create_get
from helper.permissions import IsSelfOrIsAdministrator


# views
class DoctorProfileViewSet(ModelViewSet):
    """
    View to performs -
        1. Return list of Doctors'
        2. Create New Doctor profileupdate data
        3. Update data for given doctor
        4. Delete doctor profile
    """
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    filter_class = DoctorFilter
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        certificate = request_data.get('registration_certificate')
        request_data['registration_certificate'] = certificate and decode_base64(certificate) or None

        profile_pic = request_data.get('profile_pic')
        request_data['profile_pic'] = profile_pic and decode_base64(profile_pic) or None

        resume = request_data.get('resume')
        request_data['resume'] = resume and decode_base64(resume) or None

        request_data['user'] = request.user

        try:
            # Address will be added separately (different workflow) so need to pass ID only
            if request_data.get('address'):
                request_data['address'] = Address.objects.get(id=request_data['address'])
            if request_data.get('authority_registered_with'):
                request_data['authority_registered_with'] = RegistrationAuthority.objects.get(
                    id=request_data['authority_registered_with'])

        except Address.DoesNotExist:
            Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)
        except RegistrationAuthority.DoesNotExist:
            Response(data={'error': 'Please provide valid registration authority'},
                     status=status.HTTP_400_BAD_REQUEST)

        (qualifications, specializations,
         associated_with, languages_can_speak, discipline) = (None, None, None, None, None)

        if request_data.get("qualification"):
            qualifications = validate_n_get(
                class_name='Qualification', records_ids=request_data.pop("qualification"))
        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
        if request_data.get("associated_with"):
            associated_with = validate_n_get(
                class_name='Organization', records_ids=request_data.pop("associated_with"))
        if request_data.get("languages_can_speak"):
            languages_can_speak = validate_n_get(
                class_name='Language', records_ids=request_data.pop("languages_can_speak"))
        if request_data.get("discipline"):
            discipline = validate_n_get(
                class_name='Discipline', records_ids=request_data.pop("discipline"))

        for key in ('qualification', 'specialization', 'associated_with',
                    'languages_can_speak', 'discipline'):
            try:
                request_data.pop(key)
            except:
                pass

        request_data['unique_id'] = uuid.uuid4()
        # doctor_profile = DoctorProfile.objects.create(**request_data)
        doctor_profile = DoctorProfile(**request_data)
        doctor_profile.save()

        qualifications and doctor_profile.qualification.add(*qualifications)
        specializations and doctor_profile.specialization.add(*specializations)
        associated_with and doctor_profile.associated_with.add(*associated_with)
        languages_can_speak and doctor_profile.languages_can_speak.add(*languages_can_speak)
        discipline and doctor_profile.discipline.add(*discipline)

        return Response(
            data={'success': True, 'result': self.serializer_class(doctor_profile).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data

        certificate = request_data.get('registration_certificate')
        if certificate and certificate.get('base64'):
            instance.registration_certificate = decode_base64(certificate)

        profile_pic = request_data.get('profile_pic')
        if profile_pic and profile_pic.get('base64'):
            instance.profile_pic = decode_base64(profile_pic)

        resume = request_data.get('resume')
        if resume and resume.get('base64'):
            instance.resume = decode_base64(resume)

        if request_data.get('address'):
            # Address will be added separately (different workflow) so need to pass ID only
            try:
                instance.address_id = request_data['address']
            except Address.DoesNotExist:
                Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)

        if request_data.get('authority_registered_with'):
            try:
                request_data['authority_registered_with'] = RegistrationAuthority.objects.get(
                    id=request_data['authority_registered_with'])
            except RegistrationAuthority.DoesNotExist:
                Response(data={'error': 'Please provide valid registration authority'},
                         status=status.HTTP_400_BAD_REQUEST)

        if request_data.ge('achievement_research'):
            instance.achievement_research = request_data['achievement_research']

        instance.save()
        if request_data.get("qualification"):
            qualifications = validate_n_get(
                class_name='Qualification', records_ids=request_data.pop("qualification"))
            qualifications and instance.qualification.add(*qualifications)
        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
            specializations and instance.specialization.add(*specializations)
        if request_data.get("achievement_research"):
            instance.achievement_research = request_data["achievement_research"]

        if request_data.get("associated_with"):
            associated_with = validate_n_get(
                class_name='Organization', records_ids=request_data.pop("associated_with"))
            associated_with and instance.associated_with.add(*associated_with)
        if request_data.get("languages_can_speak"):
            languages_can_speak = validate_n_get(
                class_name='Language', records_ids=request_data.pop("languages_can_speak"))
            languages_can_speak and instance.languages_can_speak.add(*languages_can_speak)

        if request_data.get("discipline"):
            discipline = validate_n_get(
                class_name='Discipline', records_ids=request_data.pop("discipline"))
            discipline and instance.discipline.add(*discipline)

        return Response(data={'success': True}, status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request):
        # TODO- not implemented
        pass


class HealthworkerProfileViewSet(ModelViewSet):
    queryset = HealthworkerProfile.objects.all()
    serializer_class = HealthworkerProfileSerializer
    filter_class = HealthworkerFilter
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        certificate = request_data.get('registration_certificate')
        request_data['registration_certificate'] = certificate and decode_base64(certificate) or None

        profile_pic = request_data.get('profile_pic')
        request_data['profile_pic'] = profile_pic and decode_base64(profile_pic) or None

        resume = request_data.get('resume')
        request_data['resume'] = resume and decode_base64(resume) or None

        try:
            request_data['address'] = Address.objects.get(id=request_data['address'])
            request_data['user'] = UserModel.objects.get(id=request_data['user'])

        except Address.DoesNotExist:
            Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)
        except UserModel.DoesNotExist:
            Response(data={'error': 'Please provide valid user'}, status=status.HTTP_400_BAD_REQUEST)

        qualifications = validate_n_get(
            class_name='Qualification', records_ids=request_data.pop("qualification"))
        associated_with = validate_n_get(
            class_name='Organization', records_ids=request_data.pop("associated_with"))
        languages_can_speak = validate_n_get(
            class_name='Language', records_ids=request_data.pop("languages_can_speak"))

        healthworker_profile = HealthworkerProfile(**request_data)
        healthworker_profile.save()

        qualifications and healthworker_profile.qualification.add(*qualifications)
        associated_with and healthworker_profile.associated_with.add(*associated_with)
        languages_can_speak and healthworker_profile.languages_can_speak.add(*languages_can_speak)

        return Response(
            data={'success': True, 'result': self.serializer_class(healthworker_profile).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data

        certificate = request_data.get('registration_certificate')
        if certificate and certificate.get('base64'):
            instance.registration_certificate = decode_base64(certificate)

        profile_pic = request_data.get('profile_pic')
        if profile_pic and profile_pic.get('base64'):
            instance.profile_pic = decode_base64(profile_pic)

        resume = request_data.get('resume')
        if resume and resume.get('base64'):
            instance.resume = decode_base64(resume)

        if request_data['address']:
            try:
                instance.address_id = request_data['address']
            except Address.DoesNotExist:
                Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)

        instance.save()

        if request_data["qualification"]:
            qualifications = validate_n_get(
                class_name='Qualification', records_ids=request_data.pop("qualification"))
            qualifications and instance.qualification.add(*qualifications)
        if request_data["associated_with"]:
            associated_with = validate_n_get(
                class_name='Organization', records_ids=request_data.pop("associated_with"))
            associated_with and instance.associated_with.add(*associated_with)
        if request_data["languages_can_speak"]:
            languages_can_speak = validate_n_get(
                class_name='Language', records_ids=request_data.pop("languages_can_speak"))
            languages_can_speak and instance.languages_can_speak.add(*languages_can_speak)

        return Response(data={'success': True}, status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request):
        # TODO- not implemented
        pass


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    filter_class = PatientFilter
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        profile_pic = request_data.get('profile_pic')
        request_data['profile_pic'] = profile_pic and decode_base64(profile_pic) or None

        request_data['case_summary'] = request_data.get('case_summary')
        request_data['weight'] = request_data.get('weight')
        request_data['height'] = request_data.get('height')
        request_data['aadhaar_no'] = request_data.get('aadhaar_no')
        request_data['alternate_mobile_no'] = request_data.get('alternate_mobile_no')

        try:
            request_data['address'] = Address.objects.get(id=request_data['address'])
            request_data['user'] = UserModel.objects.get(id=request_data['user'])
            request_data['blood_group'] = BloodGroup.objects.get(id=request_data['blood_group'])

        except Address.DoesNotExist:
            Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)
        except UserModel.DoesNotExist:
            Response(data={'error': 'Please provide valid user'}, status=status.HTTP_400_BAD_REQUEST)
        except BloodGroup.DoesNotExist:
            Response(data={'error': 'Please provide valid blood group'}, status=status.HTTP_400_BAD_REQUEST)

        languages_can_speak = validate_n_get(
            class_name='Language', records_ids=request_data.pop("languages_can_speak"))

        patient_profile = PatientProfile(**request_data)
        patient_profile.save()

        languages_can_speak and patient_profile.languages_can_speak.add(*languages_can_speak)

        return Response(
            data={'success': True, 'result': self.serializer_class(patient_profile).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data

        profile_pic = request_data.get('profile_pic')
        if profile_pic and profile_pic.get('base64'):
            instance.profile_pic = decode_base64(profile_pic)

        if request_data.get('case_summary'):
            instance.case_summary = request_data.get('case_summary')
        if request_data.get('weight'):
            instance.weight = request_data.get('weight')
        if request_data.get('height'):
            instance.height = request_data.get('height')
        if request_data.get('aadhaar_no'):
            instance.aadhaar_no = request_data.get('aadhaar_no')
        if request_data.get('alternate_mobile_no'):
            instance.alternate_mobile_no = request_data.get('alternate_mobile_no')

        if request_data['address']:
            try:
                instance.address_id = request_data['address']
            except Address.DoesNotExist:
                Response(data={'error': 'Please provide valid address'}, status=status.HTTP_400_BAD_REQUEST)
        if request_data['blood_group']:
            try:
                instance.blood_group_id = request_data['blood_group']
            except Address.DoesNotExist:
                Response(data={'error': 'Please provide valid blood group'}, status=status.HTTP_400_BAD_REQUEST)

        instance.save()

        if request_data["languages_can_speak"]:
            languages_can_speak = validate_n_get(
                class_name='Language', records_ids=request_data.get("languages_can_speak"))
            languages_can_speak and instance.languages_can_speak.add(*languages_can_speak)

        return Response(data={'success': True}, status=status.HTTP_200_OK)

    @transaction.atomic
    def delete(self, request):
        # TODO- not implemented
        pass


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
        request_data = request.data.copy()
        file_name, file_field = decode_base64(request_data)
        # tmb = TestModelBase64(profile_pic=file_field, name="Testfile.txt")
        # tmb.save()
        serialzeinfo = {'profile_pic': file_field, 'name': file_name}
        serializer_ = TestModelBase64Serializer(data=serialzeinfo)
        serializer_.is_valid()
        serializer_.save()
        print file_field
