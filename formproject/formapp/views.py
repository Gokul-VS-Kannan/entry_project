from django.shortcuts import render
from .form import MyForm

# Create your views here.

def home_view(request):
    form=MyForm()
    return render(request,"home.html",{'form':form})

def showdetails(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            return render(request,"sucess.html",{'name':name,'address':address})
    else:
        form=MyForm()
        return render(request,"home.html",{'form':form})