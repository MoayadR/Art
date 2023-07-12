from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name='home' ),
    path('create-art/' , views.createArt ,name='create-art' ),
    path('create-tag/', views.createTag , name='create-tag'),
    path('view-profile/<int:id>', views.viewProfile),
    path('view-art/<int:id>', views.viewArt),
]