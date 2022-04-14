from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermissions


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractSerializer

    def get_queryset(self):
        """Return all contracts depending on the user."""
        user = self.request.user

        if hasattr(user, "salesman"):
            return Contract.objects.filter(salesmans=user.salesman)

        return Contract.objects.all()
