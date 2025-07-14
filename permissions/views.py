from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializers import PermissionSerializer, PermissionTranslationSerializer
from .models import Permission, PermissionTranslation
# Create your views here.

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('created_at')
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermissionTranslationViewSet(viewsets.ModelViewSet):
    queryset = PermissionTranslation.objects.all()
    serializer_class = PermissionTranslationSerializer
    permission_classes = [permissions.IsAuthenticated]

class TotalPermissionsUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        total_permission_pending = PermissionTranslation.objects.filter(permission__user = user,status="pending").count()
        total_permission_approved = PermissionTranslation.objects.filter(permission__user = user,status="approved").count()
        total_permission_rejected = PermissionTranslation.objects.filter(permission__user = user,status="rejected").count()

        return Response(
            {
            "total_permission_pending": total_permission_pending,
            'total_permission_approved': total_permission_approved,
            'total_permission_rejected':total_permission_rejected
            }
                        )