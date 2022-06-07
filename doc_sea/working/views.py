import imp
from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from working.models import Hospital
from working.models import PUser

# Create your views here.

def home(req):
    hospitals=Hospital.objects.all()
    
    return render(req,"working/includes/home.html",{
        'hospital':hospitals
    })

def login(req):
    username=req.POST.get('user')
    pas=req.POST.get('pas')

    #user=authenticate(req,username=username,passwordk)
    alluser=PUser.objects.filter()
    return render(req,"working/includes/login.html")

def register(req):

    if req.method == 'POST':
        name=req.POST.get('name')
        pas=req.POST.get('pass')
        query=PUser(name=name,passwordk=pas) #name and passwordk came form the models.py
        query.save()
        messages.success(req,"welcome, "+name+" your account was created")
        return redirect('login')

    return render(req,"working/includes/register.html")

def profile(req):
    return render(req,"working/includes/profile.html")