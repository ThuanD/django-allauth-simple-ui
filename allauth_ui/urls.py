from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from .settings import acc_settings
from .views import HomeView, ProfileView

urlpatterns = [
    path("", include("allauth.urls")),
    path("",
         HomeView.as_view(
             template_name=acc_settings.HOME_TEMPLATE),
         name="account_home"),
    path("profile/<pk>/change/",
         ProfileView.as_view(
             template_name=acc_settings.PROFILE_TEMPLATE),
         name="account_profile"),
    path("profile/<pk>/password/",
         RedirectView.as_view(url=reverse_lazy("account_reset_password"))),
]
