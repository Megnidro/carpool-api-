from rest_framework import serializers
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from accounts.serializers import ProfileCustomUserSerializer, CarModelSerializer

from accounts.models import CarModel


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


class CarModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'make', 'model', 'year', 'color', 'licence_number', 'is_active']
        read_only_fields = ['owner']


class CarModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year', 'color', 'licence_number']

    def create(self, validated_data):
        user_profile = self.context['request'].user.profilecustomuser
        car = CarModel.objects.create(owner=user_profile, **validated_data)
        return car
