from rest_framework import viewsets, permissions
from .models import Address, CarModel, ProfileCustomUser, Reclaim
from .permissions import IsOwnerOrReadOnly
from .serializers import AddressSerializer, CarModelSerializer, ProfileCustomUserSerializer, ReclaimSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Exemple de méthode de permission personnalisée pour vérifier les autorisations spécifiques
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]  # Seul un utilisateur authentifié peut créer
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(),
                    IsOwnerOrReadOnly()]  # Seul le propriétaire peut mettre à jour ou supprimer
        return [permissions.IsAuthenticatedOrReadOnly()]  # Lecture seule pour les utilisateurs non authentifiés

    # Méthode facultative pour obtenir le queryset basé sur l'utilisateur authentifié
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Address.objects.all()
            else:
                # Filtrer par exemple pour l'utilisateur authentifié
                return Address.objects.filter(owner=user)
        else:
            return Address.objects.none()  # Retourner un queryset vide pour les utilisateurs non authentifiés


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Exemple de méthode de permission personnalisée pour vérifier les autorisations spécifiques
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]  # Seul un utilisateur authentifié peut créer
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(),
                    IsOwnerOrReadOnly()]  # Seul le propriétaire peut mettre à jour ou supprimer
        return [permissions.IsAuthenticatedOrReadOnly()]  # Lecture seule pour les utilisateurs non authentifiés

    # Méthode facultative pour obtenir le queryset basé sur l'utilisateur authentifié
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return CarModel.objects.all()
            else:
                # Filtrer par exemple pour l'utilisateur authentifié
                return CarModel.objects.filter(owner=user)
        else:
            return CarModel.objects.none()  # Retourner un queryset vide pour les utilisateurs non authentifiés


class ReclaimViewSet(viewsets.ModelViewSet):
    queryset = Reclaim.objects.all()
    serializer_class = ReclaimSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # Exemple de permission personnalisée
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Reclaim.objects.all()
            else:
                return Reclaim.objects.filter(owner=user)
        else:
            return Reclaim.objects.none()

class ProfileCustomUserViewSet(viewsets.ModelViewSet):
    queryset = ProfileCustomUser.objects.all()
    serializer_class = ProfileCustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # Exemple de permission personnalisée
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return ProfileCustomUser.objects.all()
            else:
                return ProfileCustomUser.objects.filter(owner=user)
        else:
            return ProfileCustomUser.objects.none()
