from django.urls import path
from . import views

# url for forum
urlpatterns = [
    path('', views.forum_view, name="forumposts"),
    path('forumposts/add', views.ForumPostCreateView.as_view(), name="forumpost_add" ),
    path('forumposts/<int:pk>/details', views.ForumPostDetailView.as_view(), name='forumpost_details'),
    path('forumposts/<int:pk>/edit', views.ForumPostUpdateView.as_view(), name='forumpost_edit'),
]

app_name = "forum"