from django.shortcuts import render

# Create your views here.
def reels(request):
    return render(request, 'reel.html')
