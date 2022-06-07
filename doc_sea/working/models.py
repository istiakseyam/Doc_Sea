from django.db import models
from django.forms import PasswordInput 


# Create your models here.

class Hospital(models.Model):
    hos_name=models.CharField(max_length=400)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    logo=models.ImageField(upload_to='images')
    hos_img=models.ImageField(upload_to='images')

class PUser(models.Model):
    name=models.CharField(max_length=200)
    passwordk=models.CharField(max_length=20)
