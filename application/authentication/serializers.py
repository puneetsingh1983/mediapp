from rest_framework.serializers import ModelSerializer
from .models import AppUserModel


class AppUserModelSerializer(ModelSerializer):
    class Meta:
        model = AppUserModel
        fields = '__all__'



