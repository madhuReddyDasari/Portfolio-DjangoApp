from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is a home page")


def about(request):
    return HttpResponse("This is a about page")


def contact(request):
    return HttpResponse("This is a contact page")
