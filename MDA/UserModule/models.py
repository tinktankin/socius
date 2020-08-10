import uuid
from django.db import models
import datetime


#http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php

# Create your models here.
#MyUUIDModel is the parent table, rest all are child tables of MyUUIDModel
class MyUUIDModel(models.Model):
    Member_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class MemberProfile(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    First_Name = models.CharField(max_length=20,blank=True)
    Last_Name = models.CharField(max_length=20,blank=True)
    Profile_Pic_URL = models.ImageField(upload_to='profile_pics')
    Bio = models.TextField(blank=True)
    Tag_Line = models.TextField(blank=True)
    profile_Status = models.IntegerField(default=0) #to know how much profile does the user completed
    Status = models.TextField(blank=True)

class Phone(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    Country_Code = models.IntegerField()
    Phone = models.IntegerField() 
    Email_Id = models.EmailField(max_length=320,blank=True)


class Address(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    Dno = models.CharField(max_length=10,blank=True)
    Street = models.TextField(blank=True)
    City = models.TextField(blank=True)
    State = models.TextField(blank=True)
    Country = models.TextField(blank=True)
    Pin_Code = models.IntegerField()

class Speciality(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    speciality = models.TextField(blank=True)

class KeySKills(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    Skills = models.TextField(blank=True)

class Certificates(models.Model):
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    #add description, date of issue the certificate
    Name = models.TextField(blank=True)
    Issuing_Org = models.TextField(null=True) #who issued the certificate
    Issued_Date = models.DateField(null=True)
    Expiration_Date = models.DateField(blank=True)
    Credential_Id = models.CharField(max_length=20,blank=True)
    Credential_URL = models.URLField(max_length=200,blank=True)
    Description = models.TextField(blank=True)
    
class Testimonial(models.Model):

    # add product/services
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    #who is giving , date of the testimonial- valid date --> should not take future date, designation, location - no need of validation
    Description = models.TextField(blank=True)
    Attestant = models.TextField(blank=True) #the one who gives testimonial
    Date = models.DateField(null=True) #should not be a future date---->need to be validated
    #no need to validate
    Designation = models.TextField(blank=True) 
    Location = models.TextField(blank=True)


class Document(models.Model):
    #doc creation date, 
    #do we need to enforce security - make doc private -create a flag -->private or public
    Member_Id= models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    File_name = models.TextField(blank=True)
    Description = models.TextField(blank=True)
    Creation_Date = models.DateField(null=True)

class AcademicDetails(models.Model):
    #date, description
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    Institution_Name = models.CharField(max_length=100,blank=True)
    Degree = models.CharField(max_length=50,blank=True)
    Field_Of_Study = models.TextField(blank=True)
    Grade = models.FloatField()
    Start_Date = models.DateField(null=True)
    End_Date = models.DateField(null=True)
    Description = models.TextField(blank=True)

class Event(models.Model):
    #date of the event, link to document
    Member_Id = models.ForeignKey(MyUUIDModel,on_delete = models.CASCADE,default=0)
    Event_Title = models.TextField(blank=True)
    Timings = models.DateTimeField(null=True)
    Description = models.TextField(blank=True)
    EventDate = models.DateField(null=True)
    LinkToDoc = models.URLField(blank=True)

#To know who can access the profile of a particular person
def accessRestriction():
    pass