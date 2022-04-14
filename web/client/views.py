from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer
from .permissions import ClientPermissions


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ClientPermissions]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
