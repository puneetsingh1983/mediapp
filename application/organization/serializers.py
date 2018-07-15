from rest_framework.serializers import ModelSerializer
from .models import Organization, OrganizationType


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationTypeSerializer(ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'
