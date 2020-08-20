from django.db import models
from django.contrib.auth.models import User
import datetime
from multi_email_field.fields import MultiEmailField
from PIL import Image
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    firstName = models.CharField(max_length=20,blank=True,default='')
    lastName = models.CharField(max_length=20,blank=True,default='')
    bio = models.TextField(max_length=200, default='', blank=True)
    tagLine = models.TextField(max_length=100, blank=True,default='')
    status = models.TextField(max_length=100 ,blank=True,default='')
    def __str__(self):
        return f'{self.user.username} Profile'
    '''
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''
#Foreign Key Tables

class Skills(models.Model):
    userSkills = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userSkills',default='',null=True)
    skill = models.TextField(null=True,blank=True,max_length=100)
    speciality = models.TextField(null=True,blank=True,max_length=100)

class ContactInfo(models.Model):
    userContact = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userContact',default='',null=True)
    email = models.EmailField(default='')
    phone = PhoneNumberField(blank=True)
    #phone = models.TextField(default='',blank=True)

class Address(models.Model):
    userAddress = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userAddress',default='',null=True)
    flatNo = models.CharField(max_length=20,blank=True,default='')
    street = models.TextField(max_length=100,blank=True,default='')
    city = models.TextField(max_length=30,blank=True,default='')
    state = models.TextField(max_length=30,blank=True,default='')
    country = models.TextField(max_length=20,blank=True,default='')
    pinCode = models.IntegerField(blank=True)


class Certificate(models.Model):
    userCertificate = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userCertificate',default='',null=True)
    name = models.TextField(blank=True,default='')
    issuingOrg = models.TextField(blank=True,default='')
    issuedDate = models.DateField(null=True)
    expiryDate = models.DateField(blank=True)
    credentialId = models.TextField(blank=True,default='')
    credentialUrl = models.URLField(blank=True,default='')
    description = models.TextField(blank=True,default='')


class Testimonial(models.Model):
    userTestimonial = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userTestimonial',default='',null=True)
    attestant = models.TextField(blank=True,default='') #the one who gives testimonial
    issuedDate = models.DateField(null=True) #should not be a future date---->need to be validated
    services = models.TextField(blank=True,default='') #product/services
    #no need to validate designation and location
    designation = models.TextField(blank=True,default='') 
    location = models.TextField(blank=True,default='')
    description = models.TextField(blank=True,default='')

class Education(models.Model):
    userEducation = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userEducation',default='',null=True)
    institute = models.TextField(blank=True,default='')
    degree = models.CharField(max_length=50,blank=True,default='')
    branch = models.TextField(blank=True,default='')
    grade = models.FloatField()
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    description = models.TextField(blank=True,default='')