from rest_framework import serializers
from users.models import User 
from users.serializers import UserSerializer
from holydays.models import Holyday 
from holydays.serializers import HolydaySerializer
from permissions.models import Permission
from permissions.serializers import PermissionSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    holyday = serializers.PrimaryKeyRelatedField(
        queryset=Holyday.objects.all(),
        allow_null=True,
        required=False
    )
    permission = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'holyday', 'permission']

    def validate(self, data):
        if not data.get('holyday') and not data.get('permission'):
            raise serializers.ValidationError("Le commentaire doit être lié à un congé ou une permission.")
        if data.get('holyday') and data.get('permission'):
            raise serializers.ValidationError("Le commentaire ne peut pas être lié aux deux en même temps.")
        return data

class GetHolydayCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    holyday = HolydaySerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'holyday']

class GetPermissionCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    permission = PermissionSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'permission']