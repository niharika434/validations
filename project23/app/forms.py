from django import forms

class Studentform(forms.Form):
    sid=forms.CharField()
    sname=forms.CharField()
    email=forms.EmailField()
    