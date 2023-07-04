from .models import Post , Tag
from django.forms import ModelForm
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['love']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple,
        }

class TagForm(ModelForm):
    class Meta:
        model= Tag
        fields = '__all__'