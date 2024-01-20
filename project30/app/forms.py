from typing import Any
from django import forms
from django.core import validators



    
def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError("started with a")
    
def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError("len is more than 5")
    
def validate_for_n(data):
    if data.startswith('N'):
        raise forms.ValidationError("started with n")



class Schoolform(forms.Form):
    sname=forms.CharField(validators=[validate_for_a,validate_for_len,validate_for_n])
    sloc=forms.CharField()
    sprince=forms.CharField(validators=[validate_for_a])
    email=forms.EmailField()
    re_enter=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean(self):
        em=self.cleaned_data['email']
        re=self.cleaned_data['re_enter']
        if em!=re:
            raise forms.ValidationError("emails not matching")
        
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError("bot error")
