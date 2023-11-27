from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("This is a home page")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is a about page")
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse("This is a contact page")
    return render(request, 'contact.html')


def projects(request):
    # return HttpResponse("This is a projects page")
    return render(request, 'projects.html')
