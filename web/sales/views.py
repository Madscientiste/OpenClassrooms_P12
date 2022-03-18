from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Salesman
from .serializers import SalesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = SalesSerializer
    queryset = Salesman.objects.all()
