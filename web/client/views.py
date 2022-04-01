from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from web.support.permissions import SupportPermissions

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [SupportPermissions]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
