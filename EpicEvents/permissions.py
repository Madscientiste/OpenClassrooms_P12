from enum import Enum
from rest_framework import permissions


class BasePermissions(permissions.BasePermission):
    def is_staff(self, req):
        return req.user.is_staff

    def is_salesman(self, req):
        return hasattr(req.user, "salesman")

    def is_support(self, req):
        return hasattr(req.user, "support")

    def methods_are_safe(self, req):
        return req.method in permissions.SAFE_METHODS
