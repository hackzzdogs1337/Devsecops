from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(max_length=10)
    class Meta:
        model=User
        fields=('username','password1','password2','email')


