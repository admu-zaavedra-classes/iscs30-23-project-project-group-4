from django.db import models

# Course
# code; title; section; 
class Course(models.Model):
    code = models.CharField(max_length = 10)
    title = models.CharField(max_length = 100)
    section = models.CharField(max_length = 3)

    def __str__(self):
        return self.code + " - " + self.title
    
# Assignments
# name; description; course; perfect_score; passing_score
class Assignment(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    perfect_score = models.IntegerField(default = 0)
    passing_score = models.IntegerField(default = 0)
 

    def __str__(self):
        return self.name

    # calculates a passing score of 60% based on perfect_score
    @property
    def passing_score_calculated(self):
        return int(self.perfect_score * 0.6)

    def save(self, *args, **kwarg):
        # passing_score will be updated after save()
        self.passing_score = self.passing_score_calculated
        super(Assignment, self).save(*args, **kwarg)