from django.contrib import admin
from .models import Course, Assignment

# admin panel for Course model
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('code', 'title', 'section')
    search_fields = ('code', 'title', 'section')
    list_filter = ('code', 'title', 'section')
    
# admin panel for Assignment model
class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ('name', 'description', 'course', 'perfect_score', 'passing_score')
    search_fields = ('name', 'description', 'course')
    list_filter = ('name', 'description', 'course', 'perfect_score')


admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)