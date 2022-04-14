from rest_framework import permissions


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        is_staff = request.user.is_staff or hasattr(request.user, "salesman")
        methods_are_safe = request.method in permissions.SAFE_METHODS
        return methods_are_safe or is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or hasattr(request.user, "salesman")
