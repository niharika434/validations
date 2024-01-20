from django import forms
from app.forms import*
from app.models import*

class Topicform(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class Webpageform(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['topic_name','url','name']
        #exclude=['url']
        #labels={'topic_name':'Topic'}
        #widgets={'url':forms.PasswordInput}

class Accessrecordform(forms.ModelForm):
    class Meta():
        model=Accessrecord
        fields='__all__'