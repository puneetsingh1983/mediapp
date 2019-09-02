# imports
from drf_extra_fields.fields import Base64FileField
from rest_framework.serializers import ModelSerializer
from .models import (DoctorProfile, HealthworkerProfile, PatientProfile, MedicalRepresentative,
                     OfflineAvailability, OnlineAvailability, OutdoorAvailability,
                     ConsultationDetails, AvailabilitySchedule, TestModelBase64)
from common.serializers import AddressSerializer


class DoctorProfileSerializer(ModelSerializer):
    address = AddressSerializer()

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


class TestModelBase64Serializer(ModelSerializer):
    profile_pic = Base64FileField()
    class Meta:
        model = TestModelBase64
        fields = '__all__'


class AvailabilityScheduleSerializer(ModelSerializer):
    class Meta:
        model = AvailabilitySchedule
        fields = '__all__'


class OnlineAvailabilitySerializer(ModelSerializer):
    schedule = AvailabilityScheduleSerializer()

    class Meta:
        model = OnlineAvailability
        fields = '__all__'


class OutdoorAvailabilitySerializer(ModelSerializer):
    schedule = AvailabilityScheduleSerializer()

    class Meta:
        model = OutdoorAvailability
        fields = '__all__'


class OfflineAvailabilitySerializer(ModelSerializer):
    schedule = AvailabilityScheduleSerializer()
    
    class Meta:
        model = OfflineAvailability
        fields = '__all__'


class ConsultationDetailsSerializer(ModelSerializer):
    class Meta:
        model = ConsultationDetails
        fields = '__all__'
