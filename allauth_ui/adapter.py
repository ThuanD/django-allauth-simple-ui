from django.apps import apps
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .settings import acc_settings

User = get_user_model()


class DefaultUserAdapter:
    name = "account"

    def get_app_list(self, user):
        app_list = []
        for app_config in apps.get_app_configs():
            if user.has_module_perms(app_config.label):
                app_dict = {
                    "name": app_config.verbose_name,
                    "app_label": app_config.label,
                    "app_url": reverse_lazy(f"{self.name}_home"),
                    "has_module_perms": user.has_module_perms(app_config.label),
                    "models": self.get_models_for_app(app_config, user),
                }
                app_list.append(app_dict)
        return app_list

    def get_models_for_app(self, app_config, user):
        models = []
        for model in app_config.get_models():
            if model == User:
                models.append(self.get_user_model(user))
        return models

    def get_user_model(self, user):
        return {
            "model": User,
            "name": User._meta.verbose_name.capitalize(),
            "admin_url": reverse_lazy(
                f"{self.name}_profile", kwargs={"pk": user.pk.__str__()}
            ),
            "view_only": False,
        }

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip


def get_adapter():
    return acc_settings.ADAPTER()
