# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from .serializers import AppUserModelSerializer
from .models import AppUserModel


# Create your views here.
class AppUserViewSet(ModelViewSet):
    queryset = AppUserModel.objects.all()
    serializer_class = AppUserModelSerializer
