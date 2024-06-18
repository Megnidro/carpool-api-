from rest_framework.permissions import BasePermission


class IsDriverOrBoth(BasePermission):
    def has_permission(self, request, view):
        return request.user.profilecustomuser.role in ['driver', 'both']


class IsPassenger(BasePermission):
    def has_permission(self, request, view):
        return request.user.profilecustomuser.role == 'passenger'
