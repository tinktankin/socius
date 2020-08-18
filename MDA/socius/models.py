from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from multi_email_field.fields import MultiEmailField
# Create your models here.
class Destination(models.Model):  
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',default='destination_4.jpg')
    desc = models.TextField(default='Defualt Value')
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)

class UserList(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254,blank=True)
    coupon = models.CharField(max_length=100, blank=True, null=True)
    is_superuser = models.BooleanField(default=False,blank=True, null=True)


class memberdirectory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(default='Defualt Value')
    size = models.IntegerField(default=0)