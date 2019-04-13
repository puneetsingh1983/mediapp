# imports
from drf_extra_fields.fields import Base64FileField
from rest_framework.serializers import ModelSerializer
from .models import (DoctorProfile, HealthworkerProfile, OnlineAvailability, OutdoorAvailability,
                     OfflineAvailability, PatientProfile, MedicalRepresentative, TestModelBase64)

class DoctorProfileSerializer(ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'


class HealthworkerProfileSerializer(ModelSerializer):
    class Meta:
        model = HealthworkerProfile
        fields = '__all__'


class PatientProfileSerializer(ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'


class MRProfileSerializer(ModelSerializer):
    class Meta:
        model = MedicalRepresentative
        fields = '__all__'


class OnlineAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = OnlineAvailability
        fields = '__all__'


class OutdoorAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = OutdoorAvailability
        fields = '__all__'


class OfflineAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = OfflineAvailability
        fields = '__all__'


class TestModelBase64Serializer(ModelSerializer):
    profile_pic = Base64FileField()
    class Meta:
        model = TestModelBase64
        fields = '__all__'