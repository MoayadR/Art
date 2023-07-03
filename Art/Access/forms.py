from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=191)
    password = forms.CharField(max_length=191 , widget=forms.PasswordInput)

class RegisterForm(ModelForm):
    field_order = ['username' , 'email' , 'password']
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups' , 'user_permissions' , 'is_staff' , 'is_active' , 'is_superuser' , 'last_login' , 'date_joined']