from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
