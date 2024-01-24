from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, name):
    return HttpResponse(f'Name is: {name}')

def lists(request):
    name = 'Ali'
    age = 10
    study = 'ICS'
    courses = [ 'web Development','Python Programing','App development','Game development','Digital Marketing','Customer support' ]

    return render(request,'list.html',{'name':name , 'age':age ,'study': study,'courses': courses})

