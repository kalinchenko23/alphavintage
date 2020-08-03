from django import forms

class Main(forms.Form):
    company_name = forms.CharField(label=False, max_length=5,widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"Company symbol"}))

class Aditinal1(forms.Form):

    company_name = forms.CharField(label=False,max_length=5,widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"Company symbol"}))
    year = forms.CharField(label=" ",max_length=10,widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"Date (yyyy-mm-dd)"}))

class Exchange_form(forms.Form):
    ex_from = forms.CharField(label=False,max_length=3,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Exchange from"}))
    ex_to = forms.CharField(label=" ",max_length=3,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Exchange to"}))
