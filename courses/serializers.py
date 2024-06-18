from rest_framework import serializers
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from accounts.serializers import ProfileCustomUserSerializer, CarModelSerializer


class TripSerializer(serializers.ModelSerializer):
    driver = ProfileCustomUserSerializer(read_only=True)
    car = CarModelSerializer()

    class Meta:
        model = Trip
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    trip = TripSerializer()
    passengers = ProfileCustomUserSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class PaymentDriverBookingSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()

    class Meta:
        model = PaymentDriverBooking
        fields = '__all__'


class ReviewTripSerializer(serializers.ModelSerializer):
    trip = TripSerializer()
    reviewer = ProfileCustomUserSerializer()

    class Meta:
        model = ReviewTrip
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    driver = ProfileCustomUserSerializer()

    class Meta:
        model = Reward
        fields = '__all__'
