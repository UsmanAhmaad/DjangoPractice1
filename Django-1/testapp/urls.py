from django.urls import path 
from . import views

urlpatterns = [
    path('home/<name>/',views.home),
    path('lists/',views.lists),
]
