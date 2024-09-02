
from django.shortcuts import render
from django.http import HttpResponse
from .models import department,Doctors
from .forms import Bookingform

def home(request):

    return render(request,'home.html',)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def Departments(request):
    dict_dept={
        'dept': department.objects.all()
    }
    return render(request, 'department.html',dict_dept)
def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=Bookingform()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)
def doctors(request):
    dict_docs={
        'docs':Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)
