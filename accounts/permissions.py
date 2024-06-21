from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour autoriser uniquement les propriétaires à modifier ou supprimer l'objet.
    """
    def has_object_permission(self, request, view, obj):
        # Les autorisations de lecture sont autorisées pour n'importe qui, donc nous autorisons toujours GET, HEAD, ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # L'utilisateur doit être le propriétaire de l'objet pour pouvoir effectuer des modifications.
        return obj.owner == request.user
