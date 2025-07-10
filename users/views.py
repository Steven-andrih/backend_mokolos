from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, CreateUserByRhSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
import random
import string
from .utils import send_invitation_email
from .models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Utilisateur créé avec succès ✅"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class CreateUserByRhView(APIView):
    def post(self, request):
        data = request.data.copy()

        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        email = data.get('email')
        role = data.get('role')
        position = data.get('position')

        user = User(
            email=email,
            role=role,
            position=position,
            is_active=True
        )
        user.set_password(random_password)
        user.save()

        send_invitation_email(user.email, random_password)

        return Response({
            "message": "Utilisateur créé avec succès ✅",
            "email": user.email,
            "generated_password": random_password
        }, status=status.HTTP_201_CREATED)

