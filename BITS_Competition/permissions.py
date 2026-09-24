from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                return request.user.organiser.admin
            except:
                return False
        return False

class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

__all__ = [
    name for name in globals()
    if not name.startswith("_")
    and name not in ("BasePermission")
]