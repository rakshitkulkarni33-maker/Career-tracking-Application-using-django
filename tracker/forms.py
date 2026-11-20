from django import forms
from .models import Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email","password1","password2")
class ApplicationForm(forms.ModelForm):
    applied_date=forms.DateField(required=False,widget=forms.DateInput(attrs={"type":"date"}))
    interview_date=forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    class Meta:
        model=Application
        fields=("company","role","location","job_url","status","applied_date","interview_date","notes")
        widgets={"notes":forms.Textarea(attrs={"rows":4})}
