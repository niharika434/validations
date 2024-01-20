from django.shortcuts import render

# Create your views here.
def hobi(request):
    return render(request,'hobi.html')

def jimin(request):
    return render(request,'jimin.html')

def jin(request):
    return render(request,'jin.html')

def hobi2(request):
    return render(request,'hobi2.html')
