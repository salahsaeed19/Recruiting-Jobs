from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from job.models import freelancer, customer, job


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    
    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['card', 'country', 'image']


class FreelancerForm(forms.ModelForm):
    class Meta:
        model = freelancer
        fields = ['card', 'name_job', 'country','image','category']


class JobForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = job
        
        fields = ['title','deadline','salary','category','cover','job_nature','description']

