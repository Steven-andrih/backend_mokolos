from django.contrib import admin
from django.urls import path
from .views import ValidatePermissionView, GetPermissionView, GetTodayPermissionView

urlpatterns = [
    path('validate/<int:pk>/', ValidatePermissionView.as_view(), name='validate_permission'),
    path('list/', GetPermissionView.as_view(), name='list_permission'),
    path('permission_actual/', GetTodayPermissionView.as_view(), name='permission_actual'),
]

