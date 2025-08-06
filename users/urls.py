from django.urls import path
from .views import GetAlluserView, UpdateUserByRhView, DeleteUserByRhView

urlpatterns = [
    path('employees/', GetAlluserView.as_view(), name='get_all_users'),
    path('update/user/<int:pk>/', UpdateUserByRhView.as_view(), name='update_user_by_rh'),
    path('delete/user/<int:pk>/', DeleteUserByRhView.as_view(), name='delete_user_by_rh'),

]

