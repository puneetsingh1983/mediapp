# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from datetime import date

from django.db import models
from django.utils.text import slugify

from authentication.models import AppUserModel


GENDER = (('-', ' -- '),
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'))


def generate_slug(value):
    return slugify(value)


class BaseModel(models.Model):
    """Base Model"""

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    # TODO - make these mandatory later. Left optional as of now
    created_by = models.ForeignKey(AppUserModel, null=True, blank=True,
                                   related_name="%(class)s_created_records")
    edited_by = models.ForeignKey(AppUserModel, null=True, blank=True,
                                  related_name="%(class)s_edited_records")

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


class Country(models.Model):
    id = models.SlugField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.id = generate_slug(self.id)
        super(Country, self).save(*args, **kwargs)


class State(models.Model):
    id = models.SlugField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country)

    def __str__(self):
        return "{}_{}".format(self.id, self.country.id)

    def save(self, *args, **kwargs):
        self.id = generate_slug(self.id)
        super(State, self).save(*args, **kwargs)


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

    address_line_1 = models.CharField(max_length=100, blank=True, null=True,  help_text="Building/Flat/Plot No.")
    address_line_2 = models.CharField(max_length=50, blank=True, null=True, help_text="Area/Locality/Post")
    address_line_3 = models.CharField(max_length=50, blank=True, null=True, help_text="Street/Village")
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    # country = models.ForeignKey(Country, on_delete=models.PROTECT)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return (self.address_line_1[:10] + ", "
                + self.city + ", "
                + str(self.state))


class Language(ModelMixinForTextField, models.Model):
    """Language Model. Ex- Hindi, English, Telugu, """
    text = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.text


class BaseProfileModel(BaseModel):
    """Base Profile Model"""

    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER, default=1)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(AppUserModel, on_delete=models.PROTECT)
    unique_id = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False)
    languages_can_speak = models.ManyToManyField(Language, blank=True)

    class Meta:
        abstract = True

    @property
    def age(self):
        today = date.today()
        dob = self.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


class Discipline(ModelMixinForTextField, models.Model):
    """Discipline Model. Ex- Allopathy, Homeopathy, Telugu, """
    text = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.text

    @classmethod
    def get_records(cls, id_list):
        return cls.objects.filter(id__in=id_list)


class RegistrationAuthority(ModelMixinForTextField, models.Model):
    text = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.text


class Accreditation(ModelMixinForTextField, models.Model):
    text = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.text