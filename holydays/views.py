from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import *
from .models import Holyday
from .serializers import HolydaySerializer, ValidateHolydaySerializer

class HolydayViewSet(viewsets.ModelViewSet):
    queryset = Holyday.objects.all()
    serializer_class = HolydaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Holyday.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ValidateHolydayView(APIView):
    permission_classes = [CanValidatePermissionOrHoliday]

    @extend_schema(
        request=ValidateHolydaySerializer,
        responses={201: ValidateHolydaySerializer}
    )
    def patch(self, request, pk):
        permission = Holyday.objects.get(pk=pk)
        self.check_object_permissions(request, permission)

        serializer = ValidateHolydaySerializer(permission, data = request.data, partial=True)
        if serializer.is_valid():
            permission = serializer.save()
            return Response({"message": "Congé valide avec succes ✅"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetHolydayView(APIView):
    permission_classes = [IsRh]

    def get(self, request):
        holydays = Holyday.objects.all().order_by("request_date")
        self.check_permissions(request)
        serializer = HolydaySerializer(holydays, many=True)
        return Response(serializer.data)