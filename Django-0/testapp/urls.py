from django.urls import path 
from . import views

urlpatterns = [
    path('main/',views.main),
    path('test/',views.test),
    path('details/<name>/',views.details),
    path('lists/',views.lists)
]