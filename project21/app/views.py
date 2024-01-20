from django.shortcuts import render
from app.models import*
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        br=request.POST['br']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,brand=br)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}

    if request.method=='POST':
        na=request.POST['na']
        mf=request.POST['mf']
        ex=request.POST['ex']

        WO=Webpage.objects.get(name=na)
        AO=Accessrecord.objects.get_or_create(name=WO,mfg=mf,exp=ex)[0]
        AO.save()

        QLAO=Accessrecord.objects.all()
        d1={'acessrecords':QLAO}
        return render(request,'display_acess.html',d1)

    

    return render(request,'insert_access.html',d)