from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
         return self.name

class Recipe(models.Model):
     title = models.CharField(max_length=30)
     description = models.TextField()
     time = models.CharField(max_length=20)
     instuctions = models.TextField()
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
     def __str__(self):
         return self.title
     