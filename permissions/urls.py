from django.contrib import admin
from django.urls import path
from .views import TotalPermissionsUserView

urlpatterns = [
    path('total/', TotalPermissionsUserView.as_view(), name="total_permission_user"),
    
]

