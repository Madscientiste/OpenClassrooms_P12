from django.db.models import base
from rest_framework import routers
from django.urls import include, path

from .views import SupportViewSet

# /api/clients/ & /api/clients/<pk>/
router = routers.DefaultRouter()
router.register(r"supports", SupportViewSet, basename="supports")

urlpatterns = [path(r"", include(router.urls))]
