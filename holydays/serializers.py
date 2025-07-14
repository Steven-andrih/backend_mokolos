from rest_framework import serializers
from .models import Holyday

class HolydaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holyday
        fields = ['id', 'start_date', 'end_date', 'leave_reasons', 'status', 'total']
        read_only_fields = ['status', 'total']

