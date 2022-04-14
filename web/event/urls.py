from django.db.models import base
from rest_framework import routers
from django.urls import include, path

from .views import EventViewSet

# /api/events/ & /api/events/<pk>/
router = routers.DefaultRouter()
router.register(r"events", EventViewSet, basename="events")

urlpatterns = [path(r"", include(router.urls))]
