from django.contrib import admin
from .models import Covoiturage, Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward

@admin.register(Covoiturage)
class CovoiturageAdmin(admin.ModelAdmin):
    pass  # Vous pouvez personnaliser cela si vous ajoutez des champs à ce modèle

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('driver', 'car', 'status', 'start_location', 'end_location', 'start_time', 'seats')
    list_filter = ('status', 'start_time')
    search_fields = ('driver__user__email', 'start_location', 'end_location')
    date_hierarchy = 'start_time'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('trip', 'passengers', 'status', 'booked_at')
    list_filter = ('status', 'booked_at')
    search_fields = ('trip__driver__user__email', 'passengers__user__email')
    date_hierarchy = 'booked_at'

@admin.register(PaymentDriverBooking)
class PaymentDriverBookingAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_method', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_method', 'payment_date')
    search_fields = ('booking__trip__driver__user__email', 'booking__passengers__user__email')
    date_hierarchy = 'payment_date'

@admin.register(ReviewTrip)
class ReviewTripAdmin(admin.ModelAdmin):
    list_display = ('trip', 'reviewer', 'rating', 'reviewed_at')
    list_filter = ('rating', 'reviewed_at')
    search_fields = ('trip__driver__user__email', 'reviewer__user__email', 'comment')
    date_hierarchy = 'reviewed_at'

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('driver', 'reward_type', 'reward_date')
    list_filter = ('reward_type', 'reward_date')
    search_fields = ('driver__user__email', 'description')
    date_hierarchy = 'reward_date'