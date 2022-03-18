from django.db.models import base
from rest_framework import routers
from django.urls import include, path

from .views import ContractViewSet

# /api/clients/ & /api/clients/<pk>/
router = routers.DefaultRouter()
router.register(r"contracts", ContractViewSet, basename="contracts")

urlpatterns = [path(r"", include(router.urls))]
