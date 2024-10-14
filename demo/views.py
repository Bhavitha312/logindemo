from django.shortcuts import render
from django.http import HttpResponse 
from demo.forms import loginform

# Create your views here.
def display(req):
    form=loginform()
    return render(req,'test.html',{'form':form})
