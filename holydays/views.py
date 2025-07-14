from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .models import Holyday
from .serializers import HolydaySerializer

class HolydayViewSet(viewsets.ModelViewSet):
    queryset = Holyday.objects.all()
    serializer_class = HolydaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Holyday.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
