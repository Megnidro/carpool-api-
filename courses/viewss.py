from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from .validators import TripValidator, BookingValidator, PaymentDriverBookingValidator, ReviewTripValidator, RewardValidator
from .permissions import IsDriverOrBoth, IsPassengerOrBoth, IsPassenger


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
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


@api_view(['GET'])
@permission_classes([IsPassengerOrBoth])
def read_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return Response({
        "driver": trip.driver_id,
        "car": trip.car_id,
        "status": trip.status,
        "start_location": trip.start_location,
        "end_location": trip.end_location,
        "start_time": trip.start_time,
        "end_time": trip.end_time,
        "seats": trip.seats,
        "distance": trip.distance
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    trip_data = request.data
    validator = TripValidator(**trip_data)
    validator.dict()  # This will raise validation errors if any

    trip.driver_id = validator.driver_id
    trip.car_id = validator.car_id
    trip.status = validator.status
    trip.start_location = validator.start_location
    trip.end_location = validator.end_location
    trip.start_time = validator.start_time
    trip.end_time = validator.end_time
    trip.seats = validator.seats
    trip.distance = validator.distance

    trip.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    trip.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsPassenger])
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


@api_view(['GET'])
@permission_classes([IsPassengerOrBoth])
def read_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return Response({
        "trip": booking.trip_id,
        "passengers": booking.passengers_id,
        "status": booking.status,
        "booked_at": booking.booked_at,
        "updated_at": booking.updated_at
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsPassenger])
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking_data = request.data
    validator = BookingValidator(**booking_data)
    validator.dict()  # This will raise validation errors if any

    booking.trip_id = validator.trip_id
    booking.passengers_id = validator.passengers_id
    booking.status = validator.status
    booking.booked_at = validator.booked_at
    booking.updated_at = validator.updated_at

    booking.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsPassenger])
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
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


@api_view(['GET'])
@permission_classes([IsDriverOrBoth])
def read_payment(request, payment_id):
    payment = get_object_or_404(PaymentDriverBooking, pk=payment_id)
    return Response({
        "booking": payment.booking_id,
        "amount": payment.amount,
        "payment_method": payment.payment_method,
        "payment_status": payment.payment_status,
        "payment_date": payment.payment_date,
        "created_at": payment.created_at,
        "updated_at": payment.updated_at
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_payment(request, payment_id):
    payment = get_object_or_404(PaymentDriverBooking, pk=payment_id)
    payment_data = request.data
    validator = PaymentDriverBookingValidator(**payment_data)
    validator.dict()  # This will raise validation errors if any

    payment.booking_id = validator.booking_id
    payment.amount = validator.amount
    payment.payment_method = validator.payment_method
    payment.payment_status = validator.payment_status
    payment.payment_date = validator.payment_date
    payment.created_at = validator.created_at
    payment.updated_at = validator.updated_at

    payment.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_payment(request, payment_id):
    payment = get_object_or_404(PaymentDriverBooking, pk=payment_id)
    payment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
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


@api_view(['GET'])
@permission_classes([IsPassengerOrBoth])
def read_review(request, review_id):
    review = get_object_or_404(ReviewTrip, pk=review_id)
    return Response({
        "trip": review.trip_id,
        "reviewer": review.reviewer_id,
        "rating": review.rating,
        "comment": review.comment,
        "reviewed_at": review.reviewed_at,
        "updated_at": review.updated_at
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_review(request, review_id):
    review = get_object_or_404(ReviewTrip, pk=review_id)
    review_data = request.data
    validator = ReviewTripValidator(**review_data)
    validator.dict()  # This will raise validation errors if any

    review.trip_id = validator.trip_id
    review.reviewer_id = validator.reviewer_id
    review.rating = validator.rating
    review.comment = validator.comment
    review.reviewed_at = validator.reviewed_at
    review.updated_at = validator.updated_at

    review.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_review(request, review_id):
    review = get_object_or_404(ReviewTrip, pk=review_id)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
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


@api_view(['GET'])
@permission_classes([IsDriverOrBoth])
def read_reward(request, reward_id):
    reward = get_object_or_404(Reward, pk=reward_id)
    return Response({
        "driver": reward.driver_id,
        "reward_type": reward.reward_type,
        "reward_date": reward.reward_date,
        "description": reward.description
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_reward(request, reward_id):
    reward = get_object_or_404(Reward, pk=reward_id)
    reward_data = request.data
    validator = RewardValidator(**reward_data)
    validator.dict()  # This will raise validation errors if any

    reward.driver_id = validator.driver_id
    reward.reward_type = validator.reward_type
    reward.reward_date = validator.reward_date
    reward.description = validator.description

    reward.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_reward(request, reward_id):
    reward = get_object_or_404(Reward, pk=reward_id)
    reward.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
