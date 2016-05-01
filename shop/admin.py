from django.contrib import admin
from django.apps import apps
shop = apps.get_app_config('shop')

for model in shop.models.values():
    admin.site.register(model)
