from rest_framework import serializers
from .models import Permission, PermissionTranslation

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionTranslation
        fields = '__all__'

    