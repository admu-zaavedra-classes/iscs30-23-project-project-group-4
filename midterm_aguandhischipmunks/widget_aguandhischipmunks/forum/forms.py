from django import forms
from .models import ForumPost

class AddForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = '__all__'
        # template to be used by default is called ForumPost_form.html