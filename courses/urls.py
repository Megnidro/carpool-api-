from django.urls import path
from . import views
from .views import TripSearchAPIView, CarModelViewSet

urlpatterns = [
    # URLs for Trip model
    path('trips/', views.TripListCreateAPIView.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', views.TripDetailAPIView.as_view(), name='trip-detail'),
    path('trips/search/', TripSearchAPIView.as_view(), name='trip-search'),

    # URLs for Booking model
    path('bookings/', views.BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingDetailAPIView.as_view(), name='booking-detail'),

    # URLs for PaymentDriverBooking model
    path('payments/', views.PaymentDriverBookingListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', views.PaymentDriverBookingDetailAPIView.as_view(), name='payment-detail'),

    # URLs for ReviewTrip model
    path('reviews/', views.ReviewTripListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewTripDetailAPIView.as_view(), name='review-detail'),

    # URLs for Reward model
    path('rewards/', views.RewardListCreateAPIView.as_view(), name='reward-list-create'),
    path('rewards/<int:pk>/', views.RewardDetailAPIView.as_view(), name='reward-detail'),

    # Liste et création de voitures
    path('api/cars/', CarModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='car-list'),

    # Détails, mise à jour et suppression d'une voiture spécifique
    path('api/cars/<int:pk>/', CarModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='car-detail'),

    # Liste des voitures actives
    path('api/cars/active/', CarModelViewSet.as_view({
        'get': 'active_cars'
    }), name='car-active'),

    # Sélection d'une voiture spécifique
    path('api/cars/<int:pk>/select/', CarModelViewSet.as_view({
        'post': 'select_car'
    }), name='car-select'),
]
