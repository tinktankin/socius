from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from multi_email_field.fields import MultiEmailField

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to='pics',default='userprofile.jpg')
    firstName = models.CharField(max_length=20,blank=True,default='',null=True)
    lastName = models.CharField(max_length=20,blank=True,default='',null=True)
    bio = models.TextField(default='', blank=True)
    tagLine = models.TextField(blank=True,default='')
    status = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user