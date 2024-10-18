from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class registerStudentForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=44)
    last_name = forms.CharField(max_length=44)

    class Meta:
        model=User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
