from rest_framework import serializers
from .models import Holyday, CalculateHolyday
from users.serializers import UserSerializer
class HolydaySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Holyday
        fields = ['id', 'request_date', 'start_date', 'end_date', 'leave_reasons', 'status', 'total', 'user','created_at', "updated_at"]
        read_only_fields = ['status']

class ValidateHolydaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holyday
        fields = ['status']

class CalculateHolydaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculateHolyday
        fields = ['weekendOption', 'startDate', 'endDate']
