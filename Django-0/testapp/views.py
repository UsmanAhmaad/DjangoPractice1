from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse('<h1>Hello World!</h1>')


# render from templates:
def test(request):
    # return HttpResponse('hello')
    return render(request,'test.html')

# <name>
def details(request,name):
    return HttpResponse(f'The name given is: {name} ')

# lists :
def lists(request):
    name = 'Ali'
    age = 20
    courses = ['web Development','Python Programing','App development','Game development','Digital Marketing','Customer support']
    course1 = courses[:3]
    course2 = courses[3:]
    return render(request,'list.html',{'name': name,'age':age, 'courses':courses ,'course1':course1,'course2':course2})
    # return render(request,'display.html',{'name':name,'age':age,'courses1':courses1 ,'courses2':courses2})
