from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializers import PermissionSerializer, ValidatePermissionSerializer
from .models import Permission
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import *
from rest_framework import status
from users.utils import send_response_permission_email
from users.models import User
from django.shortcuts import get_object_or_404
from datetime import date

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Permission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ValidatePermissionView(APIView):
    permission_classes = [CanValidatePermissionOrHoliday]

    @extend_schema(
        request=ValidatePermissionSerializer,
        responses={201: ValidatePermissionSerializer}
    )
    def patch(self, request, pk):
        # permission = Permission.objects.get(pk=pk)
        permission = get_object_or_404(Permission, pk=pk)

        self.check_object_permissions(request, permission)
        user = User.objects.get(pk=permission.user.id)

        serializer = ValidatePermissionSerializer(permission, data = request.data, partial=True)
        if serializer.is_valid():
            permission = serializer.save()
            # send_response_permission_email(user, permission)
            return Response({"message": "Permissions mise à jour avec succes ✅"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPermissionView(APIView):
    permission_classes = [IsRh]

    def get(self, request):
        permissions = Permission.objects.all().order_by("request_date")
        self.check_permissions(request)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

class GetTodayPermissionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=PermissionSerializer,
        responses={200: PermissionSerializer}
    )
    def get(self, request):
        current_date = date.today()
        permissions = Permission.objects.filter(status='approved', start_date__lte=current_date, end_date__gte=current_date)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)