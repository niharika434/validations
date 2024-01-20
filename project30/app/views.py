from django.shortcuts import render
from app.forms import *
from app.models import*
from django.http import HttpResponse


# Create your views here.
def insert_school(request):
    ESFO=Schoolform()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sl=SFDO.cleaned_data['sloc']
            sp=SFDO.cleaned_data['sprince']
            em=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['re_enter']

            SO=School.objects.get_or_create(sname=sn,sloc=sl,sprince=sp,email=em,re_enter=re)[0]
            SO.save()

            return  HttpResponse("school is installed")
        
        else:
            return HttpResponse("invalid")
    return render(request,'insert_school.html',d)
