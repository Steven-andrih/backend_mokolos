from rest_framework import serializers
from .models import Holyday
from users.serializers import UserSerializer    
class HolydaySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Holyday
        fields = ['id', 'start_date', 'end_date', 'leave_reasons', 'status', 'total', 'user']
        read_only_fields = ['status', 'total']

class ValidateHolydaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holyday
        fields = ['status']