from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, MeView, CreateUserByRhView    
from permissions.views import PermissionViewSet
from holydays.views import HolydayViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'holyday', HolydayViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/create_employer/', CreateUserByRhView.as_view(), name='create_employer'),
    # path('api/me/', MeView.as_view(), name='me'),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/', include(router.urls)),

    path("api/permissions/rh/", include('permissions.urls')),
    path("api/holyday/rh/", include('holydays.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
    