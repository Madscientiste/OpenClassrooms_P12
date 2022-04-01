from rest_framework import permissions

# Read only access to all clients, contracts or events.
# EDIT/READ to all clients that the user is responsible for


class SupportPermissions(permissions.BasePermission):
    pass
