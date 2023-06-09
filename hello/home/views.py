from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


# def index(request):
#     return HttpResponse('this is home page')

def index(request):
    context = {
        'variable': "this is msg sent"
    }
    return render(request, 'index.html', context)

# def about(request):
#     return HttpResponse('this is about page')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is service page')


def contact(request):
    if request.method == "Post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact1 = Contact(name=name, email=email, phone=phone,desc=desc, date=datetime.today())
        contact1.save()
        messages.success(request, "msg has been sent.")
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')
