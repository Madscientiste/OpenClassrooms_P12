from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
