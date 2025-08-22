from django.db import models

# Create your models here.

class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_desc=models.TextField()
    
    def __str__(self):
        return self.dept_name
    

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_Specialization=models.CharField(max_length=100)
    doctor_dept=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors/')
    
    def __str__(self):
        return self.doctor_name
    
    
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    batch=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name