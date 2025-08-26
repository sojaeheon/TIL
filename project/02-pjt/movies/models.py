from django.conf import settings
from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    popularity = models.FloatField()
    budget = models.IntegerField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    

class Cast(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    character = models.CharField(max_length=50)
    order = models.IntegerField()
    
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    content = models.TextField()
    rating = models.FloatField()
    
    
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie, related_name='genres')