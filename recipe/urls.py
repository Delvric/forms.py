from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    
    path('recipes/<int:id>/', views.recipe_detail),
    path('authors/<int:id>/', views.author_detail),
    path('addauthor/', views.authoradd_detail, name="authoradd_detail"),
    path('addrecipe/', views.recipeAddForm)
    path('login/', views.longview)

    #path('admin/', admin.site.urls),
]