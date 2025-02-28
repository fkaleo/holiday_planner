from django.contrib import admin
from .models import Destination, Trip, TripStop


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    search_fields = ("name",)


class TripStopInline(admin.TabularInline):
    model = TripStop
    extra = 1
    fields = ("destination", "arrival_datetime", "departure_datetime")


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("id", "start_datetime", "end_datetime")
    list_filter = ("start_datetime", "end_datetime")
    inlines = [TripStopInline]


@admin.register(TripStop)
class TripStopAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "destination",
        "trip",
        "arrival_datetime",
        "departure_datetime",
    )
    list_filter = ("arrival_datetime", "departure_datetime", "destination")
    search_fields = ("destination__name",)
    autocomplete_fields = ("destination",)
