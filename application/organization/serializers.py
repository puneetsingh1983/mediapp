from rest_framework.serializers import ModelSerializer
from .models import Organization, OrganizationType
from common.serializers import AddressSerializer


class OrganizationSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationTypeSerializer(ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'
