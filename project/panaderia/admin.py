from django.contrib import admin

from .models import Panaderia


@admin.register(Panaderia)
class PanaderiaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponible")
    list_filter = ("disponible",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

