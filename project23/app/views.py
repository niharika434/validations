from django.shortcuts import render
from app.forms import*
from app.models import*

# Create your views here.
def insert_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
         si=SFDO.cleaned_data['sid']
         sn=SFDO.cleaned_data['sname']
         em=SFDO.cleaned_data['email']
         SO=Student.objects.get_or_create(sid=si,sname=sn,email=em)[0]
         SO.save()

         SQO=Student.objects.all()
         d1={'SQO':SQO}
         return render(request,'display_student.html',d1)
    return render(request,'insert_student.html',d)
