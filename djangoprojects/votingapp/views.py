from django.shortcuts import render
from django.http import HttpResponse
from . import views
globalcount = dict()

# Create your views here.


def index(request):
    arr = ['Python', 'JavaScript', 'Java']
    mydictionary = {
        "arr" :arr
    }
    return render(request, 'index.html',context=mydictionary)

def getquery(request):
    q = request.GET['']
    return HttpResponse(q)
