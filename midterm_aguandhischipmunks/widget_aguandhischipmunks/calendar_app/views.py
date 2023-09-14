from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Event, Location

# calendar view for FBV implmentation
def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

#calendar Detail View for CBV Implementation
class EventDetailView(DetailView):
    model = Event
    template_name = 'event-details.html'

class EventAddListView(CreateView):
    model = Event
    template_name = "event-add.html"
    fields = "__all__"

# calendar for editing CBV implementation. 
class EventEditView(UpdateView):
    model = Event
    template_name = 'event-edit.html'
    fields = "__all__"

