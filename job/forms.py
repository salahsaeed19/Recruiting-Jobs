from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from job.models import freelancer

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    # address = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]

