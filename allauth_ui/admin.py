from django.contrib import admin
from django.urls import reverse_lazy

admin.site.site_url = reverse_lazy("account_home")
