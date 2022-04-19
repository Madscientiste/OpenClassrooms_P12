from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import UserModel
from .serializers import UserSerializer
from .permissions import UserPermissions


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated, UserPermissions]
    serializer_class = UserSerializer
