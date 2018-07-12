# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from .serializers import AppUserModelSerializer
from .models import AppUserModel


# Create your views here.
class AppUserViewSet(ModelViewSet):
    queryset = AppUserModel.objects.all()
    serializer_class = AppUserModelSerializer

    @transaction.atomic
    def create(self, request):
        request_data = request.data
        request_data.setdefault("is_staff", True)
        request_data.setdefault("is_admin", False)
        request_data.setdefault("user_type", 5)
        request_data.setdefault("user_status", 1)
        _user = AppUserModel.objects.create_user(**request_data)
        _user.save()

    @transaction.atomic
    def update(self, request, pk=None):
        pass

    @transaction.atomic
    def partial_update(self, request, pk=None):
        pass

