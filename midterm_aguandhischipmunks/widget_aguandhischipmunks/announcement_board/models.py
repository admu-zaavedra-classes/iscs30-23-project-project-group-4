from django.db import models
from dashboard.models import WidgetUser
from django.urls import reverse

# Announcement
# title; body; author; pub_datetime 
class Announcement(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=420)
    author = models.ForeignKey(WidgetUser, on_delete=models.CASCADE)
    pub_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return (reverse('announcement_board:announcement_details', kwargs={'pk' : self.pk}))


# Reaction
# name; tally; announcement;  
class Reaction(models.Model):
    name = models.CharField(max_length=100)
    tally = models.IntegerField(default=0)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
