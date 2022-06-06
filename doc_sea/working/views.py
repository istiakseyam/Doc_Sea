from django.shortcuts import render

from working.models import Hospital

# Create your views here.

def home(req):
    hospitals=Hospital.objects.all()
    
    return render(req,"working/includes/home.html",{
        'hospital':hospitals
    })

