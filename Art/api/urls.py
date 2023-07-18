from django.urls import path 
from . import views

urlpatterns = [
    path('tags/' , views.showAllTags , name='show-tags'),
    path('user/my-id' , views.showMyID , name='show-myID'),
    path('profile-data/<int:id>' , views.showMyProfileData , name='show-profiledata'),
]