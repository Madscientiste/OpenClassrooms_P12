from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermissions


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()