from rest_framework import permissions
from auth_.models import MyUser
SAFE_METHODS = ['GET',]
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            return request.user.role ==1
        return False


