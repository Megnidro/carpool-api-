from django.urls import path
from . import views

urlpatterns = [
    path('trips/create/', views.create_trip, name='create_trip'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('payments/create/', views.create_payment, name='create_payment'),
    path('reviews/create/', views.create_review, name='create_review'),
    path('rewards/create/', views.create_reward, name='create_reward'),
]
