from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import Department, WidgetUser

# dashboard view from .models
def dashboard_view(request):
    users = WidgetUser.objects.all()
    return render(request, 'dashboard.html', {'users': users})
    

class WidgetUserDetailView(DetailView):
    model = WidgetUser
    template_name = "widgetuser-details.html"


class WidgetUserCreateView(CreateView):
    model = WidgetUser
    template_name = "widgetuser-add.html"
    fields = "__all__"

class WidgetUserUpdateView(UpdateView):
    model = WidgetUser
    template_name = "widgetuser-edit.html"
    fields = "__all__"



