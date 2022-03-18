from django.db.models import base
from rest_framework import routers
from django.urls import include, path

from .views import SalesViewSet

# /api/clients/ & /api/clients/<pk>/
router = routers.DefaultRouter()
router.register(r"sales", SalesViewSet, basename="sales")

urlpatterns = [path(r"", include(router.urls))]
