from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Salesman
from .serializers import SalesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesSerializer
    queryset = Salesman.objects.all()
