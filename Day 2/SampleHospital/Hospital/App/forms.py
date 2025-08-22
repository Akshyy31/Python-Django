from django import forms
from .models import Students

class SampleForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','email','batch']
  