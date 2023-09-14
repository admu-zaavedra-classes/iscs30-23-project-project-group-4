from django.contrib import admin
from .models import ForumPost, Reply

class ReplyInLine(admin.TabularInline):
    model = Reply

# admin panel for Forum model
class ForumPostAdmin(admin.ModelAdmin):
    model = ForumPost
    list_display = ("title", "author", "body", "pub_datetime")
    inlines = [ReplyInLine]

# admin panel for Reply model
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("forum_post", "author", "body", "pub_datetime")


admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(Reply, ReplyAdmin)
