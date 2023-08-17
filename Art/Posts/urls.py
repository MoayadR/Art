from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name='home' ),
    path('create-art/' , views.createArt ,name='create-art' ),
    path('create-tag/', views.createTag , name='create-tag'),
    path('view-profile/<int:id>', views.viewProfile , name='view-profile'),
    path('view-art/<int:id>', views.viewArt , name='view-art'),
    path("delete-art/<int:id>" , views.deleteArt , name="delete-art"),
    path("delete-reported-art/<int:id>" , views.deleteReportedArt , name="delete-reported-art"),
    path("change-art/<int:id>" , views.changeArt , name="change-art"),
    path("report-art/<int:id>" , views.reportArt , name="report-art"),
    path("edit-comment/<int:artID>/<int:id>" , views.editComment , name="edit-comment"),
    path("delete-comment/<int:artID>/<int:id>" , views.deleteComment , name="delete-comment"),
    path('view-reports/' , views.viewReports , name="view-reports"),
    path('delete-report/<int:id>' , views.deleteReport , name="delete-report"),
]