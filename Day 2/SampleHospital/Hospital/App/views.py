from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import SampleForm,StudentForm
# Create your views here.

def Home(request):
    return render(request,'index.html')

def Contact(request):
   if request.method=="POST":
       form = SampleForm(request.POST)
       print("form : ",form)
       if form.is_valid():
           username= form.cleaned_data['username']
           email=form.cleaned_data['email']
           return HttpResponse(f"username is {username} , email is {email}") 
   else:
              
        form = SampleForm()  
        
   return render(request,'contact.html',{"form":form})

def About(request):
    print(request.COOKIES)
    return render (request,'about.html')

def Docters(request):
    docters_details={
        'doctors': Doctors.objects.all()
    }
    return render (request,'docters.html',docters_details)

def Department(request):
    dept_details={
        "dept": Departments.objects.all()
    }
    return render (request,'department.html',dept_details)

def Respo(request):
    return HttpResponse(f"Https response only Request {request.method}")
    # return HttpResponse("<h1>Bridgeoonnnn</h1>")
    
def set_session(request):
    request.session['name']="Akshay"
    request.session['age']=23
    request.session['place']="Vatakara"
    return HttpResponse("success")

def student_view(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('home')
            
    else :
        
        form = StudentForm()
        
    return render(request,'students.html',{"form":form})
            
            
    


