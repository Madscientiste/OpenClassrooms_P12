from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from .models import Client
from .serializers import ClientSerializer
from .permissions import ClientPermissions


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ClientPermissions]
    serializer_class = ClientSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ["date_created", "date_updated"]
    search_fields = ["user__email", "user__first_name", "user__last_name", "phone", "mobile", "company_name"]

    queryset = Client.objects.all()
