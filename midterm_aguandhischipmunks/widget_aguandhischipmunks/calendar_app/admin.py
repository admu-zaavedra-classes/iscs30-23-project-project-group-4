from django.contrib import admin
from .models import Event, Location

# admin panel for Location model
class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("mode", "venue",)
    search_fields = ("mode", "venue",)
    list_filter = ("venue",)

# admin panel for Event model
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("target_datetime", "activity", "estimated_hours", "course", "location",)
    search_fields = ("activity", "course", "location",)


admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
