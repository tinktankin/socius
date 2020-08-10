from django.shortcuts import render
from django.http import HttpResponse
import uuid 
from .models import MyUUIDModel,MemberProfile,Phone,Address,Speciality,KeySKills,Certificates,Testimonial,Document,AcademicDetails,Event
# Create your views here.

'''
def home(request):
    return render(request,'home.html')
'''

def Profile(request):
    return render(request,'Profile.html')
    #memprofile = MemberProfile()
    #fields = ('Member_ID','First_Name','Middle_Name','Last_Name','Profile_pic_URL','Country_code','Phone','Email_id','Bio','Profile_Tag_Line','profile_status','status')

def PersonalDetails(request):
    if request.method == 'POST':
        M= MemberProfile()
        M.First_Name = request.POST['First_Name']
        M.Last_Name =  request.POST["Last_Name"]
        M.Bio =  request.POST["Bio"]
        M.Tag_Line =  request.POST["Tag_Line"]
        M.Status =  request.POST["Status"]
        M.save()

        P= Phone()
        P.Phone =  request.POST["Phone"]
        P.Email_Id =  request.POST["Email_id"]
        P.save()

        A= Address()
        A.Dno =  request.POST["Dno"]
        A.Street = request.POST["Street"]
        A.City =  request.POST["City"]
        A.State =  request.POST["State"]
        A.Country =  request.POST["Country"]
        A.Pin_Code =  request.POST["Pin_code"]
        A.save()
    return render(request,'PersonalDetails.html')

def Education(request):
    if request.method == 'POST':
        E=AcademicDetails()
        E.Institution_Name = request.POST["Institution_Name"]
        E.Degree = request.POST["Degree"]
        E.Field_Of_Study = request.POST["Field_Of_Study"]
        E.Grade = request.POST["Grade"]
        E.Start_Date = request.POST["Start_Date"]
        E.End_Date = request.POST["End_Date"]
        E.Description = request.POST["Description"]
        E.save()
    return render(request,'Education.html')

def Skills(request):
    if request.method == 'POST':
        Sk=KeySKills()
        Sk.Skills = request.POST['Skills']
        Sk.save()
        Sp= Speciality()
        Sp.speciality = request.POST['speciality']
        Sp.save()
    return render(request,'Skills.html')

def  Certifications(request):
    if request.method == 'POST':
        C = Certificates()
        C.Name =  request.POST['Name']
        C.Issuing_Org = request.POST['Issuing_Org']
        C.Issued_Date = request.POST['Issued_Date']
        C.Expiration_Date = request.POST['Expiration_Date']
        C.Credential_Id = request.POST['Credential_Id']
        C.Credential_URL = request.POST['Credential_URL']
        C.Description = request.POST['Description']
        C.save()
    return render(request,'Certifications.html')

def Testimonials(request):
    if request.method == 'POST':
        T=Testimonial()
        T.Description = request.POST['Description']
        T.Attestant = request.POST['Attestant']
        T.Date = request.POST['Date']
        T.Designation = request.POST['Designation']
        T.Location = request.POST['Location']
        T.save()
    return render(request,'Testimonials.html')

def Documents(request):
    pass

def Events(request):
    pass


    