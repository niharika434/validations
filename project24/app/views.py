from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import*

# Create your views here.
def insert_topic(request):
    ETFO=Topicforms(request.POST)
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicforms(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
        return HttpResponse('succesfull')
    
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=Webpageforms(request.POST)
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageforms(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            na=WFDO.cleaned_data['name']
            em=WFDO.cleaned_data['email']

            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,email=em)[0]
            WO.save()
        return HttpResponse('successfull')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO=Accessrecordforms(request.POST)
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessrecordforms(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=na)
            au=AFDO.cleaned_data['author']
            da=AFDO.cleaned_data['date']

            AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=da)[0]
            AO.save()
        return HttpResponse("success")
    return render(request,'insert_access.html',d)