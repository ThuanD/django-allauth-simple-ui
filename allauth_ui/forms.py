from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ProfileForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see "
            "the user’s password."
        ),
    )
    last_login = forms.DateTimeField(
        label=_("Last login"),
        widget=forms.DateTimeInput(attrs={"readonly": "readonly"})
    )
    date_joined = forms.DateTimeField(
        label=_("Date joined"),
        widget=forms.DateTimeInput(attrs={"readonly": "readonly"})
    )

    class Meta:
        model = User
        field_classes = {"username": UsernameField}
        exclude = [
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        ]
