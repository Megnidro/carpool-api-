"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, CarModelViewSet, ProfileCustomUserViewSet, ReclaimViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'carmodels', CarModelViewSet, basename='carmodel')
router.register(r'profilecustomusers', ProfileCustomUserViewSet, basename='profilecustomuser')
router.register(r'reclaims', ReclaimViewSet, basename='reclaim')

urlpatterns = [
    path('', include(router.urls)),
]
"""