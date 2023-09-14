from django.db import models
from django.urls import reverse

# Department
# dept_name; home_unit
class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    home_unit = models.CharField(max_length = 100)

    def __str__(self):
        return self.dept_name + ', ' + self.home_unit 



# WidgetUser
# first_name; middle_name; last_name; department;
class WidgetUser(models.Model):
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)


    def __str__(self):
        username = self.last_name + ", " + self.first_name + " " + self.middle_name 
        return username 

    def get_absolute_url(self):
        return (reverse('widgetusers:user_details', kwargs={'pk' : self.pk}))


