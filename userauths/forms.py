from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'phone', 'gender']
