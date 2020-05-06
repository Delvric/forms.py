from django.shortcuts import render
from news.models import Author, NewsItem
# Create your views here.
def index(request):
    recipes = NewsItem.objects.all()
    return render(request,'index.html',{"recipes":recipes})