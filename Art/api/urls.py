from django.urls import path 
from . import views

urlpatterns = [
    path('tags/' , views.showAllTags ),
    path('user/my-id' , views.showMyID ),
    path('profile-data/<int:id>' , views.showMyProfileData ),
    path('comment/create', views.createComment ),
]