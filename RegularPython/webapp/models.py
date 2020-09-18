from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    year = models.IntegerField()


class MovieImage(models.Model):
    image_url = models.CharField(max_length=500)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='images')
