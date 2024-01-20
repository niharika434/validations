from nz.views import *
from django.urls import path
app_name='hello'

urlpatterns=[

    path('williamson/', williamson, name='williamson'),
]