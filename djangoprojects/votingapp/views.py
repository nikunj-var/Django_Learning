from django.shortcuts import render
globalcount = dict()

# Create your views here.
def index(request):
    return render(request,'index.html')