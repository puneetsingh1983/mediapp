# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Models
class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class State(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)


class Country(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)


class Qualification(models.Model):
    text = models.CharField(max_length=10, unique=True)


class Specialization(models.Model):
    text = models.CharField(max_length=50, unique=True)


class Research(models.Model):
    text = models.CharField(max_length=50, unique=True)


class BloodGroup(models.Model):
    type = models.CharField(max_length=50, unique=True)


class Address(models.Model):
    address_line = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State)
    country = models.ForeignKey(Country)
    pincode = models.CharField(max_length=6)


class Language(models.Model):
    text = models.CharField(max_length=15, unique=True)



