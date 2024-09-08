from django import forms
 
class MyForm(forms.Form):
    name=forms.CharField(max_length=20)
    address=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phoneno=forms.CharField(max_length=10)