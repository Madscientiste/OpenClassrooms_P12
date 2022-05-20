from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermissions


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ["date_created", "date_updated", "amount", "payment_due"]
    search_fields = ["client__user__first_name", "client__user__email", "date_created", "amount"]

    queryset = Contract.objects.all()
