from django.contrib import admin
from news.models import NewsItem, Author

def __str__(self):
    return self.name

# Register your models here.
admin.site.register(Author)
admin.site.register(NewsItem)

def __str__(self):
    return self.title
