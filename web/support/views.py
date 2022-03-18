from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Support
from .serializers import SupportSerializer


class SupportViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = SupportSerializer
    queryset = Support.objects.all()
