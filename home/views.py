from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    context = {"name": "Madhu Reddy", "course": "Python"}
    # return HttpResponse("This is a home page")
    return render(request, 'home.html', context=context)


def about(request):
    # return HttpResponse("This is a about page")
    context = {"name": "Madhu Reddy", "course": "Python"}
    return render(request, 'about.html', context)


def contact(request):
    # return HttpResponse("This is a contact page")
    return render(request, 'contact.html')


def projects(request):
    # return HttpResponse("This is a projects page")
    return render(request, 'projects.html')
