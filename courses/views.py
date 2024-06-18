from rest_framework import generics, permissions
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from .serializers import (
    TripSerializer,
    BookingSerializer,
    PaymentDriverBookingSerializer,
    ReviewTripSerializer,
    RewardSerializer,
)
from .permissions import IsDriverOrBoth, IsPassengerOrBoth, IsPassenger


class TripListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(driver=self.request.user.profilecustomuser)


class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriverOrBoth]


class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsPassengerOrBoth]

    def perform_create(self, serializer):
        serializer.save(passengers=self.request.user.profilecustomuser)


class BookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsPassengerOrBoth]


class PaymentDriverBookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentDriverBooking.objects.all()
    serializer_class = PaymentDriverBookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriverOrBoth]


class PaymentDriverBookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentDriverBooking.objects.all()
    serializer_class = PaymentDriverBookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriverOrBoth]


class ReviewTripListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReviewTrip.objects.all()
    serializer_class = ReviewTripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user.profilecustomuser)


class ReviewTripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewTrip.objects.all()
    serializer_class = ReviewTripSerializer
    permission_classes = [permissions.IsAuthenticated, IsPassengerOrBoth]


class RewardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriverOrBoth]


class RewardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriverOrBoth]
