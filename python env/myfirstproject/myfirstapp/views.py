from django.shortcuts import render,HttpResponse
from datetime import datetime
from myfirstapp.models import Contact
from django.contrib import messages

def index (request):
    return render (request,"index.html")
    # return HttpResponse("this is home page")

def about (request):
    return render (request,"about.html")
    # return HttpResponse("this is about page")

def services (request):
    return render (request,"services.html")
    # return HttpResponse("this is services page") 

def contact (request):
    if request.method =="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=Contact(name=name, address=address, phone=phone, email=email, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent !.')
    return render (request,"contact.html")
    # return HttpResponse("this is contact page")
