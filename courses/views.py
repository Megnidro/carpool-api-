from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .filters import TripFilter
from .models import Trip, Booking, PaymentDriverBooking, ReviewTrip, Reward
from .serializers import (
    TripSerializer,
    BookingSerializer,
    PaymentDriverBookingSerializer,
    ReviewTripSerializer,
    RewardSerializer, CarModelCreateSerializer,
)
from .permissions import IsDriverOrBoth, IsPassengerOrBoth, IsPassenger
from accounts.models import CarModel
from accounts.serializers import CarModelSerializer


class TripListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TripFilter

    def perform_create(self, serializer):
        serializer.save(driver=self.request.user.profilecustomuser.customuser.last_name)


class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [AllowAny]


class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(passengers=self.request.user.profilecustomuser)


class BookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]


class PaymentDriverBookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentDriverBooking.objects.all()
    serializer_class = PaymentDriverBookingSerializer
    permission_classes = [AllowAny]


class PaymentDriverBookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentDriverBooking.objects.all()
    serializer_class = PaymentDriverBookingSerializer
    permission_classes = [AllowAny]


class ReviewTripListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReviewTrip.objects.all()
    serializer_class = ReviewTripSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user.profilecustomuser)


class ReviewTripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewTrip.objects.all()
    serializer_class = ReviewTripSerializer
    permission_classes = [AllowAny]


class RewardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [AllowAny]


class RewardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [AllowAny]


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


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return CarModelCreateSerializer
        return CarModelSerializer

    @action(detail=False, methods=['GET'])
    def active_cars(self, request):
        active_cars = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(active_cars, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def select_car(self, request, pk=None):
        car = self.get_object()
        # Ici, vous pouvez ajouter la logique pour sélectionner la voiture
        # Par exemple, vous pourriez l'associer à un trajet ou simplement la marquer comme sélectionnée
        car.is_active = True
        car.save()
        return Response({'status': 'Car selected'}, status=status.HTTP_200_OK)