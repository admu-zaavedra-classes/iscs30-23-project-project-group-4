from django.db import models
from assignments.models import Course
from django.urls import reverse

# Location Choices
location_choices = [
    ('onsite', 'ONSITE'),
    ('online', 'ONLINE'),
    ('hybrid', 'HYBRID'),
]

# Location
# mode; venue;
class Location(models.Model):
    mode = models.CharField(max_length = 50, choices = location_choices, default = 'onsite')
    venue = models.TextField(max_length = 50)

    def __str__(self):
        return self.venue

# Event
# target_datetime; activity; estimated_hours; location; course
class Event(models.Model):
    target_datetime = models.DateTimeField("Date and Time: ", max_length = 50)
    activity = models.CharField("Activity: ", max_length = 50)
    estimated_hours = models.FloatField("Estimated Hours: ", max_length = 50)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.activity
    
    def get_absolute_url(self):
        return (reverse('calendar_app:event_details', kwargs={'pk' : self.pk}))
    
#refernce for location_choices: https://stackoverflow.com/questions/31130706/dropdown-in-django-model