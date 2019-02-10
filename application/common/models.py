# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from datetime import date

from django.db import models

from authentication.models import AppUserModel


GENDER = (('-', ' -- '),
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'))

AVAILABILITY_MODE = ((1, 'Online'),
                     (2, 'Offline'),
                     (3, 'Out Door'))



class BaseModel(models.Model):
    """Base Model"""
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelMixinForTextField(object):

    @classmethod
    def create_bulk_records(cls, values, return_records=False):
        records = [cls(text=item) for item in values]
        cls.objects.bulk_create(records)
        if return_records:
            return cls.objects.filter(text__in=values)

    @classmethod
    def get_records(cls, id_list):
        return cls.objects.filter(id__in=id_list)


class State(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Qualification(ModelMixinForTextField, models.Model):
    """Qualification model. Ex- MBBS, MD etc"""
    text = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.text


class Specialization(ModelMixinForTextField, models.Model):
    """Specialization Model. Ex- Pediatric, Orthopaedic Surgery, Gynecology etc"""
    text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.text


class Research(ModelMixinForTextField, models.Model):
    """Research Model"""
    text = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.text


class BloodGroup(ModelMixinForTextField, models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type


class Address(models.Model):
    """Address Model"""
    address_line = models.CharField(max_length=100, blank=True, null=True,  help_text="Building/Flat/Plot No.")
    address_line_1 = models.CharField(max_length=50, blank=True, null=True, help_text="Area/Locality/Post")
    address_line_2 = models.CharField(max_length=50, blank=True, null=True, help_text="Street/Village")
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return (self.address_line [:10] + ", "
                + self.city + ", "
                + self.state.name + ", "
                + self.country.name)


class Language(models.Model):
    """Language Model. Ex- Hindi, English, Telugu, """
    text = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.text

    @classmethod
    def get_records(cls, id_list):
        return cls.objects.filter(id__in=id_list)


class BaseProfileModel(BaseModel):
    """Base Profile Model"""
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.OneToOneField(AppUserModel, on_delete=models.DO_NOTHING)
    unique_id = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)

    class Meta:
        abstract = True

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))