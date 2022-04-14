from enum import Enum
from rest_framework import permissions


class BasePermissions(permissions.BasePermission):
    def methods_are_safe(self, request):
        return request.method in permissions.SAFE_METHODS

    def can_write(self, request, user_type: Enum("salesman", "support")):
        return request.user.is_staff or hasattr(request.user, user_type)
