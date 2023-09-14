#dashboard/urls.py

from django.urls import path
from . import views 

# url for dashboard
urlpatterns = [
    path("", views.dashboard_view, name = "dashboard"),
    path("<int:pk>/details", views.WidgetUserDetailView.as_view(), name="user_details"),
    path("add/", views.WidgetUserCreateView.as_view(), name = "new_user"),
    path("<int:pk>/edit", views.WidgetUserUpdateView.as_view(), name="update_author"),


]
app_name = "dashboard"