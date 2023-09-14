from django.urls import path
from . import views

# url for calendar
urlpatterns = [
    path('', views.calendar_view, name='calendar_app'),
    path('events/<int:pk>/details', views.EventDetailView.as_view(), name='event_details'),
    path('events/add', views.EventAddListView.as_view(), name="new_event"),
    path('events/<int:pk>/edit', views.EventEditView.as_view(), name='update_event'),
]
app_name = "calendar_app"