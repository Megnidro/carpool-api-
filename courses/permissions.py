from rest_framework.permissions import BasePermission


class IsDriverOrBoth(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['DRIVER', 'BOTH']


class IsPassengerOrBoth(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['PASSENGER', 'BOTH']


class IsPassenger(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'PASSENGER'
