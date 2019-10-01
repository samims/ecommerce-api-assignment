from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        message = "You are already authenticated"
        return not request.user.is_authenticated
