from django.urls import path 
from . import views

urlpatterns = [
    path('tags/' , views.showAllTags ),
    path('user/my-id' , views.showMyID ),
    path('profile-data/<int:id>' , views.showMyProfileData ),
    path('comment/create', views.createComment ),
    path('post/love/<int:postID>' , views.getUserLove),
    path('post/love/add/<int:postID>' , views.addUserLove),
    path('post/love/remove/<int:postID>' , views.removeUserLove),
]