from django.urls import path
from .views import EmployeeSoldView

urlpatterns = [
    path('employeeSold/<int:fk>/', EmployeeSoldView.as_view(), name='employee_sold'),

]
