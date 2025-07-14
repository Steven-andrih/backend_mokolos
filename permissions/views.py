from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializers import PermissionSerializer
from .models import Permission
# Create your views here.

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Permission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
