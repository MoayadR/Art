from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile_Data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=191)
    password = forms.CharField(max_length=191 , widget=forms.PasswordInput)

class RegisterForm(ModelForm):
    field_order = ['username' , 'email' , 'password']
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups' , 'user_permissions' , 'is_staff' , 'is_active' , 'is_superuser' , 'last_login' , 'date_joined']
        widgets = {
            'password' : forms.PasswordInput
        }

CHOICES = [
    (True , 'Male'),
    (False , 'Female'),
]

class DataForm(ModelForm):
    class Meta:
        model = Profile_Data
        fields = '__all__'
        widgets = {
            'gender':forms.RadioSelect(choices=CHOICES)
        }
