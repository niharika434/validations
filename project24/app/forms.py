from django import forms
from app.models import*

class Topicforms(forms.Form):
    topic_name=forms.CharField()

class Webpageforms(forms.Form):
    tl=[[to.topic_name,to.topic_name]  for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    email=forms.EmailField()

class Accessrecordforms(forms.Form):
    nl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=nl)
    author=forms.CharField()
    date=forms.DateField()