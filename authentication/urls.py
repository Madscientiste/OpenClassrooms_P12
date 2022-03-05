from django.urls import include, path
from . import views

urlpatterns = [
    path("login/", views.handle_login),
    path("logout/", views.handle_logout),
]
