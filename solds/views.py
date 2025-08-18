from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from apiPermission.permissions import *
from datetime import datetime
from users.utils import send_response_conge_email
from users.models import User
from django.shortcuts import get_object_or_404
from datetime import date
from .models import Sold
from .serializers import SoldSerializer
# Create your views here.

class SoldViewSet(viewsets.ModelViewSet):
    queryset = Sold.objects.all()
    serializer_class = SoldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sold.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployeeSoldView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=SoldSerializer,
        responses={200: SoldSerializer}
    )
    def get(self, request, fk):
        employee = get_object_or_404(User, pk=fk)

        solds = Sold.objects.filter(user = employee)
        serializer = SoldSerializer(solds, many=True)
        return Response(serializer.data)