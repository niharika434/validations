from django.shortcuts import render
from app.models import*

from django.http import HttpResponse
# Create your views here.
def htmlform(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topics.html',d)

    return render(request,'htmlform.html')


def form(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        CTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=CTO,name=na,url=ur)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpages.html',d1)

    return render(request,'form.html',d)




def insert_access(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']
        CWO=Webpage.objects.get(topic_name='tn',name='na',url='ur')
        AO=Accessrecords.objects.get_or_create(name=CWO,date=da,author=au)[0]
        AO.save()
        QLAO=Accessrecords.objects.all()
        d={'accessrecords':QLAO}
        return render(request,'display_access.html',d)
    return render(request,'insert_access.html',d)