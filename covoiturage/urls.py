"""
URL configuration for covoiturage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from accounts.views import AddressViewSet, CarModelViewSet, ProfileCustomUserViewSet, ReclaimViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Carpool Covoiturage API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.litslab.net/policies/terms/",
        contact=openapi.Contact(email="dmegnidro@litslab.net"),
        license=openapi.License(name="Opensource"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'carmodels', CarModelViewSet, basename='carmodel')
router.register(r'profilecustomusers', ProfileCustomUserViewSet, basename='profilecustomuser')
router.register(r'reclaims', ReclaimViewSet, basename='reclaim')

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),  # Correction de la faute de frappe ici
    # path('accouns/', include('allauth.urls')),  # Cette ligne est commentée car elle semble inactive
    path('', include('courses.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
]