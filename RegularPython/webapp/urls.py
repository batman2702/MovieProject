from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('index/',views.index),
    path('display-movies/', views.display_movie, name='display-movies'),
    path('movies-input/', views.movies_input),
    path('delete-record/<int:id>/', views.delete_record, name='delete'),
    path('update-record/<int:id>', views.update_record, name='update'),
    path('show-images/<int:id>', views.show_images, name='showimages'),
    path('insert-images/<int:id>', views.insert_image, name='insertimage'),


]