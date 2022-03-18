from django.db.models import base
from rest_framework import routers
from django.urls import include, path

from .views import ClientViewSet

# /api/clients/ & /api/clients/<pk>/
router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet, basename="clients")

urlpatterns = [path(r"", include(router.urls))]
