from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'depts':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Emp.objects.all()
    d={'emps':QLEO}
    return render(request,'display_emp.html',d)

