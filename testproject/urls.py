from django.urls import path, include

urlpatterns = [
    path("", include("allauth_ui.urls")),
]
