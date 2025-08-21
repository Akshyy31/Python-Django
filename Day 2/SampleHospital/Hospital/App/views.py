from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'index.html')

def Contact(request):
    data={'username':"Akshay",'phone':8943945360}
    return render (request,'contact.html',data)

def About(request):
    return render (request,'about.html')

def Docters(request):
    return render (request,'docters.html')

def Department(request):
    return render (request,'department.html')

def Respo(request):
    return HttpResponse("Https response only")