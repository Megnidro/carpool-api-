from django.contrib.admin import AdminSite
from unfold.admin import ModelAdmin
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from accounts.models import ProfileCustomUser, CarModel


class CustomAdminSite(AdminSite):
    site_header = 'Covoiturage Administration'
    site_title = 'Covoiturage Admin'
    index_title = "Bienvenue dans l'administration Covoiturage"


site = CustomAdminSite(name='covoiturage_admin')


class TripAdmin(ModelAdmin):
    list_display = ('driver', 'car', 'start_location', 'end_location', 'start_time', 'status')
    list_filter = ('status', 'start_time')
    search_fields = ('driver__username', 'start_location', 'end_location')


class BookingAdmin(ModelAdmin):
    list_display = ('trip', 'passengers', 'booked_at', 'status')
    list_filter = ('status', 'booked_at')
    search_fields = ('trip__driver__username', 'passengers__username')


class PaymentDriverBookingAdmin(ModelAdmin):
    list_display = ('booking', 'amount', 'payment_method', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_date')
    search_fields = ('booking__trip__driver__username', 'booking__passengers__username')


class ReviewTripAdmin(ModelAdmin):
    list_display = ('trip', 'reviewer', 'rating', 'reviewed_at')
    list_filter = ('rating', 'reviewed_at')
    search_fields = ('trip__driver__username', 'reviewer__username')


class RewardAdmin(ModelAdmin):
    list_display = ('driver', 'reward_type', 'reward_date')
    list_filter = ('reward_type', 'reward_date')
    search_fields = ('driver__username',)


site.register(ProfileCustomUser)
site.register(CarModel)
site.register(Trip, TripAdmin)
site.register(Booking, BookingAdmin)
site.register(PaymentDriverBooking, PaymentDriverBookingAdmin)
site.register(ReviewTrip, ReviewTripAdmin)
site.register(Reward, RewardAdmin)
