from django.urls import path
from . import views

urlpatterns = [
    # URLs for Trip model
    path('trips/', views.TripListCreateAPIView.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', views.TripDetailAPIView.as_view(), name='trip-detail'),

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
]
