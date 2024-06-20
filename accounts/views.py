from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ProfileCustomUser, CarModel, Notification, Reclaim, Address
from .serializers import ProfileCustomUserSerializer, CarModelSerializer, NotificationSerializer, ReclaimSerializer, \
    AddressSerializer
from .permissions import IsDriverOrBoth, IsPassenger


class ProfileCustomUserListCreateAPIView(ListCreateAPIView):
    queryset = ProfileCustomUser.objects.all()
    serializer_class = ProfileCustomUserSerializer
    permission_classes = [IsDriverOrBoth | IsAuthenticated]


class ProfileCustomUserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProfileCustomUser.objects.all()
    serializer_class = ProfileCustomUserSerializer
    permission_classes = [IsDriverOrBoth | IsAuthenticated]


class CarModelListCreateAPIView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = AllowAny


class CarModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsDriverOrBoth | IsAuthenticated]


class NotificationListCreateAPIView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


class NotificationDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


class ReclaimListCreateAPIView(ListCreateAPIView):
    queryset = Reclaim.objects.all()
    serializer_class = ReclaimSerializer
    permission_classes = [IsAuthenticated]


class ReclaimDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reclaim.objects.all()
    serializer_class = ReclaimSerializer
    permission_classes = [IsAuthenticated]


class AddressListCreateAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsDriverOrBoth | IsAuthenticated, IsPassenger]


class AddressDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsDriverOrBoth | IsAuthenticated, IsPassenger]
