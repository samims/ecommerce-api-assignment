from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission class
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.method in SAFE_METHODS and
            request.user.is_authenticated or
            request.user
            and request.user.is_staff
        )


class IsOwner(BasePermission):
    """
    Custom permission to only allow
    owners of object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
