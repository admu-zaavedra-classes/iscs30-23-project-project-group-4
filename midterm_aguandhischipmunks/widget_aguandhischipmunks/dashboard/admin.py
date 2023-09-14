from django.contrib import admin
from .models import Department, WidgetUser


# admin panel for Department model
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    search_fields = ("dept_name", "home_unit",)
    list_display = ("dept_name", "home_unit",)
    list_filter = ("dept_name",)


# admin panel for WidgetUser model
class WidgetUserAdmin(admin.ModelAdmin):
    model = WidgetUser
    search_fields = ("first_name", "middle_name", "last_name", "department",)
    list_display = ("first_name", "middle_name", "last_name", "department",)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(WidgetUser, WidgetUserAdmin)


