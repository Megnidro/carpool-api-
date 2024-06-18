from django.urls import path
from .viewss import (
    create_trip, read_trip, update_trip, delete_trip,
    create_booking, read_booking, update_booking, delete_booking,
    create_payment, read_payment, update_payment, delete_payment,
    create_review, read_review, update_review, delete_review,
    create_reward, read_reward, update_reward, delete_reward
)

urlpatterns = [
    path('trips/', create_trip, name='create_trip'),
    path('trips/<int:trip_id>/', read_trip, name='read_trip'),
    path('trips/<int:trip_id>/update/', update_trip, name='update_trip'),
    path('trips/<int:trip_id>/delete/', delete_trip, name='delete_trip'),

    path('bookings/', create_booking, name='create_booking'),
    path('bookings/<int:booking_id>/', read_booking, name='read_booking'),
    path('bookings/<int:booking_id>/update/', update_booking, name='update_booking'),
    path('bookings/<int:booking_id>/delete/', delete_booking, name='delete_booking'),

    path('payments/', create_payment, name='create_payment'),
    path('payments/<int:payment_id>/', read_payment, name='read_payment'),
    path('payments/<int:payment_id>/update/', update_payment, name='update_payment'),
    path('payments/<int:payment_id>/delete/', delete_payment, name='delete_payment'),

    path('reviews/', create_review, name='create_review'),
    path('reviews/<int:review_id>/', read_review, name='read_review'),
    path('reviews/<int:review_id>/update/', update_review, name='update_review'),
    path('reviews/<int:review_id>/delete/', delete_review, name='delete_review'),

    path('rewards/', create_reward, name='create_reward'),
    path('rewards/<int:reward_id>/', read_reward, name='read_reward'),
    path('rewards/<int:reward_id>/update/', update_reward, name='update_reward'),
    path('rewards/<int:reward_id>/delete/', delete_reward, name='delete_reward'),
]
