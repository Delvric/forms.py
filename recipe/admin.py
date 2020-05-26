from django.contrib import admin
from recipe.models import Recipe, Author

def __str__(self):
    return self.name

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)

def __str__(self):
    return self.title
