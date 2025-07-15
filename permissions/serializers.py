from rest_framework import serializers
from .models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'start_date', 'end_date', 'beginning_hour', 'end_time', 'nature', 'status']
        read_only_fields = ['status']

class ValidatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['status']
                                                                