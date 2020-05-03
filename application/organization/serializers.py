from rest_framework.serializers import ModelSerializer
from .models import Organization, OrganizationType, Pathology
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


class PathologySerializer(ModelSerializer):
    address = AddressSerializer()
    # PathlogyLabType

    class Meta:
        model = Pathology
        fields = '__all__'
