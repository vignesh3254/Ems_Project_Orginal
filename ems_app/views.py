from django.shortcuts import render,redirect
from .models import Data
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'ems_app/index.html',{
        'emp':Data.objects.all()
    })

def view_info(request,id):
    emp=Data.objects.get(pk=id)
    return render(request,'ems_app/index.html',{'emp':emp})

def add_emp(request):
    if request.method=="POST":
        emp_id=request.POST['emp_id']
        emp_name=request.POST['emp_name']
        emp_mail=request.POST['emp_mail']
        emp_city=request.POST['emp_city']
        Data.objects.create(
            emp_id=emp_id,
            emp_name=emp_name,
            emp_mail=emp_mail,
            emp_city=emp_city
        )
        return redirect(reverse('home'))
    return redirect(reverse('home'))


def update_emp(request,id):
    emp=Data.objects.get(id=id)
    if request.method=="POST":
        emp.emp_id=request.POST['emp_id']
        emp.emp_name=request.POST['emp_name']
        emp.emp_mail=request.POST['emp_mail']
        emp.emp_city=request.POST['emp_city']
        
        emp.save()
        return redirect(reverse('home'))
    return render(request,'ems_app/index.html',{
        'emp':Data.objects.all(),
        'emp_to_update':emp
    })
    
def remove_emp(request,id):
    if request.method=="POST":
        emp=Data.objects.get(id=id)
        emp.delete()
        return redirect(reverse('home'))
    