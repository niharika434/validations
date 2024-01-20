from django.shortcuts import render

# Create your views here.
def tae(request):
    return render(request,'tae.html')

def jin(request):
    return render(request, 'jin.html')