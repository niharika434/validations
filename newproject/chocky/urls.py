from chocky.views import *
from django.urls import path
app_name='flavour'
urlpatterns = [
    path('oreo/', oreo, name='oreo'),
]