from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Announcement, Reaction


# announcemnet view for FBV implementation
def announcements_view(request):
    announcements = Announcement.objects.all().order_by('-pub_datetime') #https://www.w3schools.com/django/django_queryset_orderby.php
    return render(request, 'announcements.html', {'announcements': announcements})

# announcement detail view for CBV implementation
class AnnouncementsDetailsView(DetailView):
    model = Announcement
    template_name = 'announcement-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reactions'] = Reaction.objects.all()

        return context

# add announcement, CBV implementation
class AnnouncementsAddView(CreateView):
    model = Announcement
    fields = '__all__'
    template_name = 'announcement-add.html'

# edit announcement, CBV implementation
class AnnouncementsEditView(UpdateView):
    model = Announcement
    fields = '__all__'
    template_name = 'announcement-edit.html'



def announcement_boardIndex(request):
    announcements = Announcement.objects.all()
    reactions = Reaction.objects.all()
    announcement_board_output = "Widget’s Announcement Board <br><br> Announcements: <br>"

    for announcement in announcements:  
        datetime = announcement.pub_datetime.strftime("%m/%d/%Y, %I:%M %p")
        announcement_board_output += (announcement.title + " by " + announcement.author.first_name + 
                                      " " + announcement.author.last_name + " published " + datetime +
                                      ": <br>" + announcement.body + "<br>"
        )
        
        like_tally = 0
        love_tally = 0
        angry_tally = 0

        for reaction in reactions:
            if reaction.announcement.title == announcement.title:
                if reaction.name == "Like":
                    like_tally = reaction.tally
                elif reaction.name == "Love":
                    love_tally = reaction.tally
                elif reaction.name == "Angry":
                    angry_tally = reaction.tally
        
        announcement_board_output = (announcement_board_output + "Like: " + str(like_tally) + "<br>Love: " +
                                      str(love_tally) + "<br>Angry: " + str(angry_tally) + "<br><br>")
                
    return HttpResponse(announcement_board_output)            
                