from django.shortcuts import render, reverse
from recipe.models import Author, Recipe
from recipe.forms import RecipeAddForm, AuthorAddForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {"recipes": data})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {"recipe": recipe})
    


def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, "author.html", {"author": author, "recipes": recipes})
    

def authoradd_detail(request):
    form = AuthorAddForm()
    if request.method == "POST"():
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    return render(request, "authoraddform.html", {"form": form})
    
def recipeadd_detail(request):
    html = 'recipeaddform.html'
     if = request.method == "POST"
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time=data['time'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

        form = RecipeAddForm()

        return render(request, html, {"form": form})
        
        def authoradd(request):
            html = "generic_form.html"
            if request.method == 'POST'
            form = AuthorAddForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('homepage'))

            form = AuthorAddForm()
    

    
