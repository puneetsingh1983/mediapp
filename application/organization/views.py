# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import OrganizationType, Organization, Pathology
from .serializers import OrganizationSerializer, OrganizationTypeSerializer, PathologySerializer
from .filters import OrganizationFilter
from helper.permissions import IsSelfOrIsAdministrator
from helper.address_util import build_address
from helper.file_handler import decode_base64
from userprofile.utils import validate_n_get
from common.models import Accreditation, PathlogyLabType


# views
class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_class = OrganizationFilter
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        if request_data.get('address'):
            try:
                request_data['address'] = build_address(request_data.get('address'))
            except Exception as exp:
                return Response(data={'error': exp.message},
                                status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("associated_company"):
            try:
                request_data['associated_company'] = Organization.objects.get(
                    request_data.get("associated_company"))
            except Organization.DoesNotExist:
                return Response(data={'error': 'Please provide valid organization.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
        if request_data.get("org_type"):
            try:
                request_data['org_type'] = OrganizationType.objects.get(id=request_data.get("org_type"))
            except OrganizationType.DoesNotExist:
                return Response(data={'error': 'Please provide valid organization type.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("accreditation"):
            try:
                request_data['accreditation'] = Accreditation.objects.get(id=request_data.get("accreditation"))
            except Accreditation.DoesNotExist:
                return Response(data={'error': 'Please provide valid accreditation type.'},
                         status=status.HTTP_400_BAD_REQUEST)

        license_doc = request_data.get('license_doc')
        request_data['license_doc'] = license_doc and decode_base64(license_doc) or None

        try:
            request_data.pop("specialization")
        except:
            pass

        org = Organization(**request_data)
        org.save()

        specializations and org.specialization.add(*specializations)

        return Response(
            data={'success': True, 'result': self.serializer_class(org).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data

        license_doc = request_data.get('license_doc')
        if license_doc and license_doc.get('base64'):
            instance.license_doc = decode_base64(license_doc)

        if request_data.get('address'):
            # Address will be added separately (different workflow) so need to pass ID only
            try:
                instance.address_id = build_address(request_data.get('address'))
            except Exception as exp:
                # TODO - refactor
                return Response(data={'error': exp.message}, status=status.HTTP_400_BAD_REQUEST)

        if request_data.get('associated_company'):
            try:
                instance.associated_company = Organization.objects.get(
                    id=request_data['associated_company'])
            except Organization.DoesNotExist:
                return Response(data={'error': 'Please provide valid associated organization'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("org_type"):
            try:
                instance.org_type = OrganizationType.objects.get(id=request_data.get("org_type"))
            except OrganizationType.DoesNotExist:
                return Response(data={'error': 'Please provide valid organization type.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("accreditation"):
            try:
                instance.accreditation = Accreditation.objects.get(id=request_data.get("accreditation"))
            except Accreditation.DoesNotExist:
                return Response(data={'error': 'Please provide valid accreditation type.'},
                         status=status.HTTP_400_BAD_REQUEST)

        instance.save()

        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
            specializations and instance.specialization.add(*specializations)

        return Response(data={'success': True}, status=status.HTTP_200_OK)


class OrganizationTypeViewSet(ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)


class PathologyViewSet(ModelViewSet):
    queryset = Pathology.objects.all()
    serializer_class = PathologySerializer
    # filter_class =
    permission_classes = (IsAuthenticated, IsSelfOrIsAdministrator)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        if request_data.get('address'):
            try:
                request_data['address'] = build_address(request_data.get('address'))
            except Exception as exp:
                return Response(data={'error': exp.message},
                                status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("associated_company"):
            try:
                request_data['associated_company'] = Pathology.objects.get(
                    request_data.get("associated_company"))
            except Pathology.DoesNotExist:
                return Response(data={'error': 'Please provide valid Pathology.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
        if request_data.get("lab_type"):
            try:
                request_data['lab_type'] = PathlogyLabType.objects.get(id=request_data.get("lab_type"))
            except PathlogyLabType.DoesNotExist:
                return Response(data={'error': 'Please provide valid pathology type.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("accreditation"):
            try:
                request_data['accreditation'] = Accreditation.objects.get(id=request_data.get("accreditation"))
            except Accreditation.DoesNotExist:
                return Response(data={'error': 'Please provide valid accreditation type.'},
                         status=status.HTTP_400_BAD_REQUEST)

        license_doc = request_data.get('license_doc')
        request_data['license_doc'] = license_doc and decode_base64(license_doc) or None

        try:
            request_data.pop("specialization")
        except:
            pass

        patho = Pathology(**request_data)
        patho.save()

        specializations and patho.specialization.add(*specializations)

        return Response(
            data={'success': True, 'result': self.serializer_class(patho).data},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data

        license_doc = request_data.get('license_doc')
        if license_doc and license_doc.get('base64'):
            instance.license_doc = decode_base64(license_doc)

        if request_data.get('address'):
            # Address will be added separately (different workflow) so need to pass ID only
            try:
                instance.address_id = build_address(request_data.get('address'))
            except Exception as exp:
                # TODO - refactor
                return Response(data={'error': exp.message}, status=status.HTTP_400_BAD_REQUEST)

        if request_data.get('associated_company'):
            try:
                instance.associated_company = Pathology.objects.get(
                    id=request_data['associated_company'])
            except Pathology.DoesNotExist:
                return Response(data={'error': 'Please provide valid associated pathology'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("lab_type"):
            try:
                instance.lab_type = PathlogyLabType.objects.get(id=request_data.get("lab_type"))
            except PathlogyLabType.DoesNotExist:
                return Response(data={'error': 'Please provide valid pathology type.'},
                         status=status.HTTP_400_BAD_REQUEST)
        if request_data.get("accreditation"):
            try:
                instance.accreditation = Accreditation.objects.get(id=request_data.get("accreditation"))
            except Accreditation.DoesNotExist:
                return Response(data={'error': 'Please provide valid accreditation type.'},
                         status=status.HTTP_400_BAD_REQUEST)

        instance.save()

        if request_data.get("specialization"):
            specializations = validate_n_get(
                class_name='Specialization', records_ids=request_data.pop("specialization"))
            specializations and instance.specialization.add(*specializations)

        return Response(data={'success': True}, status=status.HTTP_200_OK)

