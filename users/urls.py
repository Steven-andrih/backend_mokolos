from django.urls import path
from .views import GetAlluserView, UpdateUserByRhView, DeleteUserByRhView, TodayEmployeeView, CongesPermissionsStatsView, StatusDistributionView

urlpatterns = [
    path('employees/', GetAlluserView.as_view(), name='get_all_users'),
    path('today_employees/', TodayEmployeeView.as_view(), name='get_today_employee'),

    path('update/user/<int:pk>/', UpdateUserByRhView.as_view(), name='update_user_by_rh'),
    path('delete/user/<int:pk>/', DeleteUserByRhView.as_view(), name='delete_user_by_rh'),

    path('stats/conges-permissions/', CongesPermissionsStatsView.as_view(), name='stats-conges-permissions'),
    path('stats/status-distribution/', StatusDistributionView.as_view(), name='status-distribution'),

]

