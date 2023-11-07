from django.contrib import admin

from .models import DutyLocation, DutyLocationName


@admin.register(DutyLocation)
class DutyLocationAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(DutyLocationName)
class DutyLocationNameAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    autocomplete_fields = ["duty_location"]
