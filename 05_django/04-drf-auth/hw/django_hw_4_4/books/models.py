from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length = 200)
    genres = models.ManyToManyfields(Genre,related_name='books')
    published_data = models.DateField()
    borrowed = models.BooleanField(default=False)
    isbn = models.CharField(max_length=13,unique=True)
    