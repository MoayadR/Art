from django.urls import path 
from . import views

urlpatterns = [
    path('tags/' , views.showAllTags , name='show-tags'),
]