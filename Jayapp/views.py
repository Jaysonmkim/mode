from django.shortcuts import render
from Jayapp.forms import StudentsForm

def index(request):
    stud=StudentsForm
    return render(request,'index.html',{'form':stud})


