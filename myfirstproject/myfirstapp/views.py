from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from .myfirstproject.myfirstapp.forms import FeedbackForm

# from myfirstproject.myfirstapp.forms import feedbackforms
from .forms import *

# Create your views here.


def myfunctioncall(request):
    return HttpResponse("hello world")


def myfunctionabout(request):
    return HttpResponse("i am about page")


def add(request, a, b):
    return HttpResponse(a+b)


def intro(request, name, age):
    mydictionary = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydictionary)


def myfirstpage(request):
    return render(request, 'index.html')


def mysecondpage(request):
    return render(request, 'second.html')


def mythirdpage(request):
    fruits = ["apple", "banana", "grapes"]
    num1, num2 = 3, 5
    ans = num1 > num2
    context = {
        "var": "inherited",
        "msg": "greetings",
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, 'mythirdpage.html', context)


def myimagepage(request):
    return render(request, 'image.html')


def myimagepage2(request):
    return render(request, 'image2.html')


def myimagepage3(request):
    return render(request, 'image3.html')


def myimagepage4(request):
    return render(request, 'image4.html')


def myform(request):
    return render(request, 'form.html')

# for GET method
# def submitmyform(request):
#     var1 = request.GET.get('mytext', '')  # Provide a default value if 'mytext' is not found
#     var2 = request.GET.get('mytextarea', '')  # Provide a default value if 'mytextarea' is not found

#     mydictionary = {
#         "var1": var1,
#         "var2": var2,
#         "method": request.method
#     }
#     return JsonResponse(mydictionary)

# for POST method


def submitmyform(request):
    # Provide a default value if 'mytext' is not found
    var1 = request.POST.get('mytext', '')
    # Provide a default value if 'mytextarea' is not found
    var2 = request.POST.get('mytextarea', '')

    mydictionary = {
        "var1": var1,
        "var2": var2,
        "method": request.method
    }
    return JsonResponse(mydictionary)


def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            # print(title)
            # print(subject)
            # var = str('form submitted' + str(request.method))
            mydictionary = {
                "form": FeedbackForm(),
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be capital"
                Errors.append(errormsg)
            import re
            # used for email checking
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "NOt a valid mail"
                Errors.append(errormsg)
                # mydictionary["error"] = True
                # mydictionary["errormsg"] = "Title should be capital"
                # return render(request, 'myform2.html', context=mydictionary)
            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "form submitted"
            # update dictionary
            mydictionary['error'] = errorflag
            mydictionary['errors'] = Errors
            return render(request, 'myform2.html', context=mydictionary)
            # return HttpResponse(var)
        else:
            mydictionary = {
                "form": form
            }
            return render(request, 'myform2.html', context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm()
        mydictionary = {
            "form": form
        }
        return render(request, 'myform2.html', context=mydictionary)


def error_404_view(request,exception):
    return render(request,'404.html')

