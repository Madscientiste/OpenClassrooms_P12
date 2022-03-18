from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
