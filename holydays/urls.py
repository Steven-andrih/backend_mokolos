from django.urls import path
from .views import ValidateHolydayView, GetHolydayView, CalculateHolydayView

urlpatterns = [
    path('validate/<int:pk>/', ValidateHolydayView.as_view(), name='validate_holyday'),
    path('list/', GetHolydayView.as_view(), name='list_holydays'),

    path('calculate/', CalculateHolydayView.as_view(), name='calculate_holyday_duration'),
]

