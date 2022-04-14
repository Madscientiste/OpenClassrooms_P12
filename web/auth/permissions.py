from rest_framework import permissions


# only staff can view & edit all users


class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
