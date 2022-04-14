from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermissions


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractSerializer

    def get_queryset(self):
        """Return all contracts for the current user. All contracts are returned if the user is an admin."""
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Contract.objects.all()

        return Contract.objects.filter(sales_contact=user.salesman)
