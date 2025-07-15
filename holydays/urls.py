from django.urls import path
from .views import ValidateHolydayView

urlpatterns = [
    path('/validate/<int:pk>', ValidateHolydayView.as_view(), name='validate_holyday')
]

