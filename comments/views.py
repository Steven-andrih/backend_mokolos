
from .serializers import CommentSerializer, GetHolydayCommentSerializer,GetPermissionCommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from holydays.models import Holyday
from permissions.models import Permission

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CommentSerializer,
        responses={200: CommentSerializer}
    )
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetHistoryCommentHolydayView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=GetHolydayCommentSerializer,
        responses={200: GetHolydayCommentSerializer}
    )
    def get(self, request, pk):
        self.check_permissions(request)
        holyday = get_object_or_404(Holyday, pk=pk)
        comments = holyday.comments.all().order_by("created_at")
        serializer = GetHolydayCommentSerializer(comments, many=True)
        return Response(serializer.data)

class GetHistoryCommentPermissionView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=GetPermissionCommentSerializer,
        responses={200: GetPermissionCommentSerializer}
    )
    def get(self, request, pk):
        self.check_permissions(request)
        permission = get_object_or_404(Permission, pk=pk)
        comments = permission.comments.all().order_by("created_at")
        serializer = GetPermissionCommentSerializer(comments, many=True)
        return Response(serializer.data)



