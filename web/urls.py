from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("web.auth.urls")),
    path("", include("web.client.urls")),
    path("", include("web.contract.urls")),
    path("", include("web.event.urls")),
    path("", include("web.sales.urls")),
    path("", include("web.support.urls")),
]
