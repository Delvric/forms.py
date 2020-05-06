from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

class NewsItem(models.Model):
     title = models.CharField(max_length=30)
     body = models.TextField()
     date = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
     def __str__(self):
         return self.title
     