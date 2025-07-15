from django.contrib import admin
from django.urls import path
from .views import ValidatePermissionView

urlpatterns = [
    path('/validate/<int:pk>', ValidatePermissionView.as_view(), name='validate_permission')
]

