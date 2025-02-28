from django.contrib import admin
from .models import Destination, Trip, TripStop

admin.site.register(Destination)
admin.site.register(TripStop)
admin.site.register(Trip)
