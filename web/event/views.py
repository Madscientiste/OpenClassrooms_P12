from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermissions


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventSerializer

    def get_queryset(self):
        """Return all events depending on the user."""
        user = self.request.user

        if hasattr(user, "support"):
            return  Event.objects.filter(support=user.support)

        return Event.objects.all()
