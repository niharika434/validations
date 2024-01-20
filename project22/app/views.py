from django.shortcuts import render
from app.forms import*
from django.http import HttpResponse

# Create your views here.
def djforms(request):

    ENFO=Nameform()
    d={'ENFO':ENFO}
    if request.method=='POST':
        NFDO=Nameform(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    
    return render(request,'djforms.html',d)