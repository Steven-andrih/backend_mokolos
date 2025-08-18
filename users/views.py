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
from datetime import date
from django.db.models import Q
from django.utils.timezone import now
from django.db.models import Count, Q
from collections import OrderedDict
from solds.models import Sold

from holydays.models import Holyday
from permissions.models import Permission
from users.models import User
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
    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer}
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class GetAlluserView(APIView):
    permission_classes = [IsRh]
    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer}
    )
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

        sold = Sold(
            user=user
        )
        sold.save()

        # send_invitation_email(user.email, random_password)

        return Response({
            "message": "Utilisateur créé avec succès ✅",
            "email": user.email,
            "generated_password": random_password,
            "first_sold":sold.id
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

class TodayEmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()

        # IDs des absents 
        holyday_ids = User.objects.filter(
            holydays__status='approved',
            holydays__start_date__lte=today,
            holydays__end_date__gte=today
        ).values_list('id', flat=True)

        permission_ids = User.objects.filter(
            permissions__status='approved',
            permissions__start_date__lte=today,
            permissions__end_date__gte=today
        ).values_list('id', flat=True)

        absents_ids = set(holyday_ids) | set(permission_ids)

        presents = User.objects.exclude(id__in=absents_ids)
        absents = User.objects.filter(id__in=absents_ids)

        presents_data = UserSerializer(presents, many=True).data
        absents_data = UserSerializer(absents, many=True).data

        return Response({
            "date": today,
            "total_present": presents.count(),
            "total_absent": absents.count(),
            "presents": presents_data,
            "absents": absents_data
        })
class CongesPermissionsStatsView(APIView):
    def get(self, request):
        current_year = now().year
        
        months = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin",
                  "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]
        
        # On prépare un dict avec 0 pour congés et permissions par mois
        stats = OrderedDict()
        for i, month in enumerate(months, start=1):
            stats[month] = {"conges": 0, "permissions": 0}

        conges = Holyday.objects.filter(
            status='approved',
            start_date__year=current_year
        ).values('start_date__month').annotate(count=Count('id'))
        
        for entry in conges:
            month_index = entry['start_date__month']
            month_name = months[month_index - 1]
            stats[month_name]['conges'] = entry['count']

        permissions = Permission.objects.filter(
            status='approved',
            start_date__year=current_year
        ).values('start_date__month').annotate(count=Count('id'))

        for entry in permissions:
            month_index = entry['start_date__month']
            month_name = months[month_index - 1]
            stats[month_name]['permissions'] = entry['count']

        data = []
        for month, values in stats.items():
            data.append({
                "name": month,
                "conges": values['conges'],
                "permissions": values['permissions'],
            })

        return Response(data)

class StatusDistributionView(APIView):
    """
    Retourne la répartition des congés et permissions par statut pour l'année en cours.
    """
    def get(self, request):
        current_year = now().year

        status_choices = ['pending', 'approved', 'rejected']

        # Congés approuvés t@ty taoan ity
        conges_stats = []
        for status in status_choices:
            count = Holyday.objects.filter(
                status=status,
                start_date__year=current_year
            ).count()
            display_name = {
                'pending': 'En attente',
                'approved': 'Approuvées',
                'rejected': 'Rejetées'
            }.get(status, status)
            conges_stats.append({
                'name': display_name,
                'value': count
            })

        # permission approuvés t@ty taoan ity
        permissions_stats = []
        for status in status_choices:
            count = Permission.objects.filter(
                status=status,
                start_date__year=current_year
            ).count()
            display_name = {
                'pending': 'En attente',
                'approved': 'Approuvées',
                'rejected': 'Rejetées'
            }.get(status, status)
            permissions_stats.append({
                'name': display_name,
                'value': count
            })

        return Response({
            'conges': conges_stats,
            'permissions': permissions_stats
        })

class StatusDistributionEmployeeView(APIView):
    """
    Retourne la répartition des congés et permissions par statut pour l'année en cours pour un user.
    """
    def get(self, request, pk):
        current_year = now().year
        user = get_object_or_404(User, pk=pk)
        status_choices = ['pending', 'approved', 'rejected']

        # Congés approuvés t@ty taoan ity
        conges_stats = []
        for status in status_choices:
            count = Holyday.objects.filter(
                status=status,
                start_date__year=current_year,
                user=user
            ).count()
            display_name = {
                'pending': 'En attente',
                'approved': 'Approuvées',
                'rejected': 'Rejetées'
            }.get(status, status)
            conges_stats.append({
                'name': display_name,
                'value': count
            })

        # permission approuvés t@ty taoan ity
        permissions_stats = []
        for status in status_choices:
            count = Permission.objects.filter(
                status=status,
                start_date__year=current_year,
                user=user
            ).count()
            display_name = {
                'pending': 'En attente',
                'approved': 'Approuvées',
                'rejected': 'Rejetées'
            }.get(status, status)
            permissions_stats.append({
                'name': display_name,
                'value': count
            })

        return Response({
            'user':user.email,
            'conges': conges_stats,
            'permissions': permissions_stats
        })
    