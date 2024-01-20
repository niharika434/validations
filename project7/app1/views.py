from django.shortcuts import render

# Create your views here.
def render_1(request):
    data= 'Hello this is new world'
    d={'world':data}
    return render(request,'render_1.html',context=d)
