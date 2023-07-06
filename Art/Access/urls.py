from django.urls import path 
from . import views

urlpatterns = [
    path('login/' , views.loginUser , name='login'),
    path('register/' , views.register , name='register'),
    path('logout/' , views.logoutUser , name='logout'),
    path('profile/' , views.showProfile , name='profile'),
    path('create-profile/<int:userID>/' , views.createProfile , name='create-profile'),
    path('edit-profile/' , views.editProfile , name='edit-profile'),
]