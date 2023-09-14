from django.urls import path
from .import views 

# url for announcement_board
urlpatterns = [
    path('', views.announcements_view, name='announcements'),
    path('add', views.AnnouncementsAddView.as_view(), name='announcement_add'),
    path('<int:pk>/details', views.AnnouncementsDetailsView.as_view(), name='announcement_details'),
    path('<int:pk>/edit', views.AnnouncementsEditView.as_view(), name='announcement_edit'),
]
app_name = "announcement_board"