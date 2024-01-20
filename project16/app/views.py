from django.shortcuts import render

# Create your views here.
def own(request):
    return render(request,'own.html')
