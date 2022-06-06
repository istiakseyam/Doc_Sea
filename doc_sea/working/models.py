from django.db import models

# Create your models here.

class Hospital(models.Model):
    hos_name=models.CharField(max_length=400)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    logo=models.ImageField(upload_to='images')
    hos_img=models.ImageField(upload_to='images')
    