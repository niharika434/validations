from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'Niharika','class':'btech','stream':'ECE'}
    return render(request,'forloop.html',context=d)
