from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from .validators import TripValidator, BookingValidator, PaymentDriverBookingValidator, ReviewTripValidator, RewardValidator


@api_view(['POST'])
def create_trip(request):
    trip_data = request.data
    validator = TripValidator(**trip_data)
    validator.dict()  # This will raise validation errors if any
    trip = Trip.objects.create(
        driver_id=validator.driver_id,
        car_id=validator.car_id,
        status=validator.status,
        start_location=validator.start_location,
        end_location=validator.end_location,
        start_time=validator.start_time,
        end_time=validator.end_time,
        seats=validator.seats,
        distance=validator.distance
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_booking(request):
    booking_data = request.data
    validator = BookingValidator(**booking_data)
    validator.dict()  # This will raise validation errors if any
    booking = Booking.objects.create(
        trip_id=validator.trip_id,
        passengers_id=validator.passengers_id,
        status=validator.status,
        booked_at=validator.booked_at,
        updated_at=validator.updated_at
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_payment(request):
    payment_data = request.data
    validator = PaymentDriverBookingValidator(**payment_data)
    validator.dict()  # This will raise validation errors if any
    payment = PaymentDriverBooking.objects.create(
        booking_id=validator.booking_id,
        amount=validator.amount,
        payment_method=validator.payment_method,
        payment_status=validator.payment_status,
        payment_date=validator.payment_date,
        created_at=validator.created_at,
        updated_at=validator.updated_at
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_review(request):
    review_data = request.data
    validator = ReviewTripValidator(**review_data)
    validator.dict()  # This will raise validation errors if any
    review = ReviewTrip.objects.create(
        trip_id=validator.trip_id,
        reviewer_id=validator.reviewer_id,
        rating=validator.rating,
        comment=validator.comment,
        reviewed_at=validator.reviewed_at,
        updated_at=validator.updated_at
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_reward(request):
    reward_data = request.data
    validator = RewardValidator(**reward_data)
    validator.dict()  # This will raise validation errors if any
    reward = Reward.objects.create(
        driver_id=validator.driver_id,
        reward_type=validator.reward_type,
        reward_date=validator.reward_date,
        description=validator.description
    )
    return Response(status=status.HTTP_201_CREATED)
