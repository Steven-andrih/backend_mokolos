from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'position', 'first_name', 'last_name', 'description']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'role', 'position', 'first_name', 'last_name', 'description']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CreateUserByRhSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','role', 'position', 'first_name', 'last_name', 'description']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)