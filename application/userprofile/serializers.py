# imports
from drf_extra_fields.fields import Base64FileField
from rest_framework.serializers import ModelSerializer
from .models import DoctorProfile, HealthworkerProfile, Availability, PatientProfile, MedicalRepresentative, TestModelBase64
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


class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class TestModelBase64Serializer(ModelSerializer):
    profile_pic = Base64FileField()
    class Meta:
        model = TestModelBase64
        fields = '__all__'