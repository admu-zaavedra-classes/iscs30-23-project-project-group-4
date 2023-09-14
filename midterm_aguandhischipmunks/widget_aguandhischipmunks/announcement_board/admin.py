from django.contrib import admin
from .models import Announcement, Reaction


class ReactionInline(admin.TabularInline):
    model = Reaction

# admin panel for Announcemnet model
class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    
    search_fields = ('title', 'author',)
    list_display = ('title', 'body', 'author', 'pub_datetime',)
    list_filter = ('title', 'author', 'pub_datetime',)
    inlines = [ReactionInline,]

# admin panel for Reaction model
class ReactionAdmin(admin.ModelAdmin):
    model = Reaction

    search_fields = ('name', 'announcement',)
    list_display = ('name', 'tally', 'announcement',)
    list_filter = ('name', 'tally',)

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Reaction, ReactionAdmin)
