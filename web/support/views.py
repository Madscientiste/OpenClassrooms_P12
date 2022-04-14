from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Support
from .serializers import SupportSerializer


class SupportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SupportSerializer
    queryset = Support.objects.all()
