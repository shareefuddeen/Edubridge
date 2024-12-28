from django import forms
from .models import Assignments,Submission

class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields=['title','description','due_date']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model=Submission
        fields=['content']

