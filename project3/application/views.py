from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def niharika(request):
    return HttpResponse("<h1><marquee>Hello Friends</h1></marquee>")
