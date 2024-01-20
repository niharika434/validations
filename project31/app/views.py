from django.shortcuts import render
from app.forms import*
from django.http import HttpResponse
# Create your views here.
def create_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse("done")
        else:
            return HttpResponse("invalid")
    return render(request,'create_student.html',d)
