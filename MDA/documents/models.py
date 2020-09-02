from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class Document(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userdocument',default='',null=True)
    fileName = models.CharField(max_length=100, blank=True,default='')
    uploadFile = models.FileField(upload_to='documents')
    description = models.TextField(blank=True,default='')
    uploadedOn = models.DateTimeField(auto_now_add=True,null=True)
    fileExtension = models.TextField(default='',null=True)
    