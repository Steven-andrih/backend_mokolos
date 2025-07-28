from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import *
from .models import Holyday
from .serializers import HolydaySerializer, ValidateHolydaySerializer, CalculateHolydaySerializer
from .utils import getHolydayDuration
from datetime import datetime
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
    
class CalculateHolydayView(APIView):

    @extend_schema(
        request=CalculateHolydaySerializer,
        responses={201: CalculateHolydaySerializer}
    )
    def post(self, request):
        data = request.data.copy()

        weekendOption = data.get('weekendOption')
        startDateStr = data.get('startDate')   # string : "2025-07-28"
        endDateStr = data.get('endDate')       # string : "2025-07-30"

        try:
            # Convertir string en objet datetime.date
            startDate = datetime.strptime(startDateStr, "%Y-%m-%d").date()
            endDate = datetime.strptime(endDateStr, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Format de date invalide. Format attendu : YYYY-MM-DD"}, status=400)

        total_days = getHolydayDuration(weekendOption, startDate, endDate)

        return Response({
            "message": "Durée de congés calculée avec succès ✅",
            "total_days": total_days
        }, status=status.HTTP_201_CREATED)
