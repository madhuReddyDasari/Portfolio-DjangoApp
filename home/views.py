from django.shortcuts import render, HttpResponse
from home import models
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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['description']
        # print(name, email, phone, desc)
        rec_obj = models.Contact(
            name=name, email=email, phone=phone, description=desc)
        rec_obj.save()
        print("Record inserted into DB.")
    # return HttpResponse("This is a contact page")
    return render(request, 'contact.html')


def projects(request):
    # return HttpResponse("This is a projects page")
    return render(request, 'projects.html')
