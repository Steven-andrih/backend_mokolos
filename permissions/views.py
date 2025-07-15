from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializers import PermissionSerializer, ValidatePermissionSerializer
from .models import Permission
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import *
from rest_framework import status

# Create your views here.
# class RegisterView(APIView):
#     @extend_schema(
#         request=RegisterSerializer,
#         responses={201: RegisterSerializer}
#     )
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "Utilisateur créé avec succès ✅"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        permission = Permission.objects.get(pk=pk)
        self.check_object_permissions(request, permission)

        serializer = ValidatePermissionSerializer(permission, data = request.data, partial=True)
        if serializer.is_valid():
            permission = serializer.save()
            return Response({"message": "Permissions valide avec succes ✅"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPermissionView(APIView):
    permission_classes = [IsRh]

    def get(self, request):
        permissions = Permission.objects.all().order_by("request_date")
        self.check_permissions(request)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)