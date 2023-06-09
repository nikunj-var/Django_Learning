from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("hello world")

def myfunctionabout(request):
    return HttpResponse("i am about page")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')