from rest_framework import serializers
from .models import Permission
from users.serializers import UserSerializer
class PermissionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Permission
        fields = ['id', 'start_date', 'end_date', 'beginning_hour', 'end_time', 'nature', 'status', 'user']
        read_only_fields = ['status']

class ValidatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['status']
                                                                