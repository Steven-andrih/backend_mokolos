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
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import IsRh
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
class RegisterView(APIView):
    @extend_schema(
        request=RegisterSerializer,
        responses={201: RegisterSerializer}
    )
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

class GetAlluserView(APIView):
    permission_classes = [IsRh]

    def get(self, request):
        users = User.objects.all()
        self.check_permissions(request)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class CreateUserByRhView(APIView):
    @extend_schema(
        request=CreateUserByRhSerializer,
        responses={201: CreateUserByRhSerializer}
    )
    def post(self, request):
        data = request.data.copy()

        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        email = data.get('email')
        role = data.get('role')
        position = data.get('position')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        description = data.get('description')

        user = User(
            first_name = first_name,
            last_name = last_name,
            description = description,
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
    
class UpdateUserByRhView(APIView):
    @extend_schema(
        request=CreateUserByRhSerializer,
        responses={200: CreateUserByRhSerializer}
    )
    def patch(self, request, pk):
        user = User.objects.get(pk=pk)

        serializer = CreateUserByRhSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User mise à jour avec succes ✅"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserByRhView(APIView):
    permission_classes = [IsAuthenticated, IsRh]
    authentication_classes = [JWTAuthentication]
    
    def delete(self, request, pk):
        self.check_permissions(request)
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({
            "message": "Utilisateur supprimer avec succès ✅",
        }, status=status.HTTP_200_OK)

        
