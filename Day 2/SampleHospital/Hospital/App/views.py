from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'base.html')

def Contact(request):
    data={'username':"Akshay",'phone':8943945360}
    return render (request,'contact.html',data)

def About(request):
    return render (request,'about.html')

def Docters(request):
    return render (request,'docters.html')

def Department(request):
    return render (request,'department.html')
