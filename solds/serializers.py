from rest_framework import serializers
from users.models import User 
from users.serializers import UserSerializer
from .models import Sold

class SoldSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Sold
        fields = ['id', 'user', 'year', 'sold']