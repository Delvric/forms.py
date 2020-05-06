from django.urls import path

from news import views

urlpatterns = [
    path('', views.index),
    #path('admin/', admin.site.urls),
]