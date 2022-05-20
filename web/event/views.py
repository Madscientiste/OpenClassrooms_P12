from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermissions


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ["date_created", "date_updated", "attendees", "event_date"]
    search_fields = ["client__company_name"]
