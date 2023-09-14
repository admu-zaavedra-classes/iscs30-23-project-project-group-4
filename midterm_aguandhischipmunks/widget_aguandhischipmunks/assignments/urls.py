from django.urls import path
from . import views

# url for assignments
urlpatterns = [
    path('', views.assignments_view, name='assignment'),
    path('add', views.AssignmentAddListView.as_view(), name="assignment_add" ),
    path('<int:pk>/details', views.AssignmentDetailView.as_view(), name='assignment_details'),
    path('<int:pk>/edit', views.AssignmentEditView.as_view(), name='assignment_edit'),
]