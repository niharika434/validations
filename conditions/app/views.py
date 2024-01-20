from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'a':400,'b':200,'c':600}
    return render(request,'cond.html',d)
