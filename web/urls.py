from django.urls import include, path
from .views import auth

urlpatterns = [
    path("login/", auth.handle_login),
    path("logout/", auth.handle_logout),
]
