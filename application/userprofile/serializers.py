from rest_framework.serializers import ModelSerializer
from .models import DoctorProfile, HealthworkerProfile, Availability, PatientProfile


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


class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
