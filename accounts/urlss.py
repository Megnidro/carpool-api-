# urlss.py
from django.urls import path, include

from .viewss import (
    create_user, read_user, update_user, delete_user,
    create_profile, read_profile, update_profile, delete_profile,
    create_car, read_car, update_car, delete_car,
    create_notification, read_notification, update_notification, delete_notification,
    create_reclaim, read_reclaim, update_reclaim, delete_reclaim,
    create_address, read_address, update_address, delete_address
)
urlpatterns = [

    path('accounts/', include('allauth.urls')),

    path('user/', create_user, name='create_user'),
    path('user/<int:user_id>/', read_user, name='read_user'),
    path('user/<int:user_id>/update/', update_user, name='update_user'),
    path('user/<int:user_id>/delete/', delete_user, name='delete_user'),

    # ProfileCustomUser URLs
    path('profile/', create_profile, name='create_profile'),
    path('profile/<int:profile_id>/', read_profile, name='read_profile'),
    path('profile/<int:profile_id>/update/', update_profile, name='update_profile'),
    path('profile/<int:profile_id>/delete/', delete_profile, name='delete_profile'),

    # CarModel URLs
    path('car/', create_car, name='create_car'),
    path('car/<int:car_id>/', read_car, name='read_car'),
    path('car/<int:car_id>/update/', update_car, name='update_car'),
    path('car/<int:car_id>/delete/', delete_car, name='delete_car'),

    # Notification URLs
    path('notification/', create_notification, name='create_notification'),
    path('notification/<int:notification_id>/', read_notification, name='read_notification'),
    path('notification/<int:notification_id>/update/', update_notification, name='update_notification'),
    path('notification/<int:notification_id>/delete/', delete_notification, name='delete_notification'),

    # Reclaim URLs
    path('reclaim/', create_reclaim, name='create_reclaim'),
    path('reclaim/<int:reclaim_id>/', read_reclaim, name='read_reclaim'),
    path('reclaim/<int:reclaim_id>/update/', update_reclaim, name='update_reclaim'),
    path('reclaim/<int:reclaim_id>/delete/', delete_reclaim, name='delete_reclaim'),

    # Address URLs
    path('address/', create_address, name='create_address'),
    path('address/<int:address_id>/', read_address, name='read_address'),
    path('address/<int:address_id>/update/', update_address, name='update_address'),
    path('address/<int:address_id>/delete/', delete_address, name='delete_address'),
]
