from rest_framework.serializers import ModelSerializer
from .models import AppUserModel


class AppUserModelSerializer(ModelSerializer):
    class Meta:
        model = AppUserModel
        fields = ['id', 'username', 'mobile', 'user_type', 'user_status',
                  'full_name', 'reason_for_modification', 'full_name', 'is_otp_verified']


