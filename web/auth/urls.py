from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from django.urls import include, path

from .views import UsersViewSet

# /api/users/ & /api/users/<pk>/
router = routers.DefaultRouter()
router.register(r"users", UsersViewSet, basename="users")

urlpatterns = [
    path(r"", include(router.urls)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
