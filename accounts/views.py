from rest_framework import viewsets, permissions
from .models import Address, CarModel, ProfileCustomUser, Reclaim
from .serializers import AddressSerializer, CarModelSerializer, ProfileCustomUserSerializer, ReclaimSerializer
from .permissions import IsOwnerOrReadOnly  # Import de la permission personnalisée si nécessaire

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # Utilisation de la permission personnalisée si besoin
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        return Address.objects.all()


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # Utilisation de la permission personnalisée si besoin
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        return CarModel.objects.all()


class ProfileCustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ProfileCustomUser.objects.filter(user=user)


class ReclaimViewSet(viewsets.ModelViewSet):
    queryset = Reclaim.objects.all()
    serializer_class = ReclaimSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # Utilisation de la permission personnalisée si besoin
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        return Reclaim.objects.all()
