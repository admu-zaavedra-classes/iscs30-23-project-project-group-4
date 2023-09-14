from django.db import models
from dashboard.models import WidgetUser
from django.urls import reverse

# Forum Post
# title; body; author; pub_datetime;
class ForumPost(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField(max_length = 1000)
    author = models.ForeignKey(WidgetUser, on_delete = models.CASCADE)
    pub_datetime = models.DateTimeField("Published Date and Time", auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:forumpost_details', kwargs={'pk':self.pk})

# Reply
# body; author; pub_datetime; forum_post;
class Reply(models.Model):
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(WidgetUser, on_delete=models.CASCADE)
    pub_datetime = models.DateTimeField("Published Date and Time", auto_now_add=True)
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
