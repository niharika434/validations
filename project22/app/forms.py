from django import forms

class Nameform(forms.Form):
    sname=forms.CharField()
    sloc=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':8}))
    gender=forms.ChoiceField(choices=[('male','male'),('female','female')])
    course=forms.MultipleChoiceField(choices=[('python','python'),('java','java'),('c++','c++')],widget=forms.CheckboxSelectMultiple)
