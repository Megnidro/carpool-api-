# models.py
from django.db import models
from accounts.models import ProfileCustomUser

from accounts.models import CarModel


# le conducteur cree de trajet, et le passant aussi creé son trajet

class Covoiturage(models.Model):
    pass


class Trip(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELLED', 'CANCELLED'),
    )
    driver = models.ForeignKey(ProfileCustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='trips')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    distance = models.FloatField()

    class Meta:
        unique_together = (('driver', 'car'),)
        indexes = [
            models.Index(fields=['driver', 'car']),
        ]

        #spatial index
        indexes += [
            models.Index(fields=['start_location', 'end_location']),

        ]

    def __str__(self):
        return f'{self.car} - {self.driver} - {self.start_location} - {self.end_location}'

    def validate_driver(self):
        if self.driver.ProfileCustomUser.role == 'driver':
            return True
        else:
            return (f'{self.driver.ProfileCustomUser.role} you must a driver to create this trip. Please contact your '
                    f'administrator.')


class Booking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('CONFIRMED', 'CONFIRMED'),
        ('CANCELLED', 'CANCELLED'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    passengers = models.ForeignKey(ProfileCustomUser, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('trip', 'passengers'),)
        indexes = [
            models.Index(fields=['trip', 'passengers']),
        ]


class PaymentDriverBooking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('CONFIRMED', 'CONFIRMED'),
        ('CANCELLED', 'CANCELLED'),
        ('PAID', 'PAID'),
        ('FREE', 'FREE'),
    )
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    payment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewTrip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(ProfileCustomUser, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(decimal_places=2, max_digits=10)
    comment = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reviewer} - {self.trip} - {self.rating} - {self.comment}'

    class meta:
        verbose_name_plural = 'ReviewTrips'
        verbose_name = 'ReviewTrip'


class Reward(models.Model):
    driver = models.ForeignKey(ProfileCustomUser, on_delete=models.CASCADE, related_name='rewards')
    reward_type = models.CharField(max_length=10)
    reward_date = models.DateTimeField()
    description = models.TextField()
