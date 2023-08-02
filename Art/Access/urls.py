from django.urls import path 
from . import views

urlpatterns = [
    path('login/' , views.loginUser , name='login'),
    path('register/' , views.register , name='register'),
    path('logout/' , views.logoutUser , name='logout'),
    path('profile/' , views.showProfile , name='profile'),
    path('create-profile/<int:userID>/' , views.createProfile , name='create-profile'),
    path('edit-profile/' , views.editProfile , name='edit-profile'),
    path('edit-account/' , views.editAccount , name = 'edit-account'),
    path('edit-account/firstname' , views.editFirstName , name = 'edit-account-first-name'),
    path('edit-account/lastname' , views.editLastName , name = 'edit-account-last-name'),
    path('edit-account/email' , views.editEmail, name = 'edit-account-email'),
    path('edit-account/password' , views.editPassword, name = 'edit-account-password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]