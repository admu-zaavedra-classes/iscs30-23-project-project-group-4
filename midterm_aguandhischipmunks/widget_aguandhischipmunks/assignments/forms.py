from django import forms
from .models import Assignment

class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['passing_score']


