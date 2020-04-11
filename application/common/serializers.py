from rest_framework.serializers import ModelSerializer

from .models import (Country, State, Qualification,
                     Language, Specialization,
                     BloodGroup, Address, Research, Discipline,
                     RegistrationAuthority, Accreditation)


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class SpecializationSerializer(ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class BloodGroupSerializer(ModelSerializer):
    class Meta:
        model = BloodGroup
        fields = '__all__'


class ResearchSerializer(ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'


class DisciplineSerializer(ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class RegistrationAuthoritySerializer(ModelSerializer):
    class Meta:
        model = RegistrationAuthority
        fields = '__all__'


class AccreditationSerializer(ModelSerializer):
    class Meta:
        model = Accreditation
        fields = '__all__'