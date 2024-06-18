from django.urls import path
from .views import (
    ProfileCustomUserListCreateAPIView,
    ProfileCustomUserDetailAPIView,
    CarModelListCreateAPIView,
    CarModelDetailAPIView,
    NotificationListCreateAPIView,
    NotificationDetailAPIView,
    ReclaimListCreateAPIView,
    ReclaimDetailAPIView,
    AddressListCreateAPIView,
    AddressDetailAPIView,
)

urlpatterns = [
    # ProfileCustomUser endpoints
    path('profile-users/', ProfileCustomUserListCreateAPIView.as_view(), name='profile-user-list'),
    path('profile-users/<int:pk>/', ProfileCustomUserDetailAPIView.as_view(), name='profile-user-detail'),

    # CarModel endpoints
    path('car-models/', CarModelListCreateAPIView.as_view(), name='car-model-list'),
    path('car-models/<int:pk>/', CarModelDetailAPIView.as_view(), name='car-model-detail'),

    # Notification endpoints
    path('notifications/', NotificationListCreateAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),

    # Reclaim endpoints
    path('reclaims/', ReclaimListCreateAPIView.as_view(), name='reclaim-list'),
    path('reclaims/<int:pk>/', ReclaimDetailAPIView.as_view(), name='reclaim-detail'),

    # Address endpoints
    path('addresses/', AddressListCreateAPIView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', AddressDetailAPIView.as_view(), name='address-detail'),
]
