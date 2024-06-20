from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(driver=self.request.user.profilecustomuser.customuser.last_name)


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


class TripSearchAPIView(APIView):
    def get(self, request):
        start_location = request.query_params.get('start_location', None)
        end_location = request.query_params.get('end_location', None)
        min_seats = request.query_params.get('min_seats', None)
        max_seats = request.query_params.get('max_seats', None)

        # Construire le queryset initial
        queryset = Trip.objects.all()

        # Appliquer les filtres en fonction des paramètres de requête
        if start_location:
            queryset = queryset.filter(start_location__icontains=start_location)
        if end_location:
            queryset = queryset.filter(end_location__icontains=end_location)
        if min_seats:
            queryset = queryset.filter(seats__gte=min_seats)
        if max_seats:
            queryset = queryset.filter(seats__lte=max_seats)

        # Sérialiser les résultats
        serializer = TripSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Récupérer les données du corps de la requête POST
        start_location = request.data.get('start_location', None)
        end_location = request.data.get('end_location', '')
        min_seats = request.data.get('min_seats', None)
        max_seats = request.data.get('max_seats', None)

        # Filtrer les trajets en fonction des critères fournis
        queryset = Trip.objects.all()

        if start_location:
            queryset = queryset.filter(start_location__icontains=start_location)
        if end_location:
            queryset = queryset.filter(end_location__icontains=end_location)
        if min_seats is not None:
            queryset = queryset.filter(seats__gte=min_seats)
        if max_seats is not None:
            queryset = queryset.filter(seats__lte=max_seats)

        # Serializer les résultats
        serializer = TripSerializer(queryset, many=True)

        # Retourner la réponse JSON avec les données filtrées
        return Response(serializer.data, status=status.HTTP_200_OK)
        