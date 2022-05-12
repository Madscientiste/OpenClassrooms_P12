from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermissions


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
