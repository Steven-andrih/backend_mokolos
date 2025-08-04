from django.urls import path
from .views import GetAlluserView

urlpatterns = [
    path('employees/', GetAlluserView.as_view(), name='get_all_users'),
]

