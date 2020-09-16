from django import forms
from .models import Profile,profilePic,Skills,Speciality,Certificate,Testimonial,Education
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = "date"
    input_formats = "dd/mm/yyyy"

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName','lastName','email','altEmail','phone','altPhone','address','city','state','country','postalCode','aboutMe']
        labels = {
            'firstName':'First Name',
            'lastName':'Last Name',
            'email':'Email',
            'altEmail':'Alternate Email',
            'phone':'Phone number',
            'altPhone':'Alternate Phone number',
            'address':'Address',
            'city': 'City',
            'state':'State',
            'country':'Country',
            'postalCode':'Postal Code',
            'aboutMe':'About Me'
        }

class ProfilePicForm(ModelForm):
    class Meta:
        model = profilePic
        fields = ['image','status','tagLine']
        labels = {
            'image':'upload picture',
            'status':'Status',
            'tagLine':'Tag Line'
        }
       
class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']
        labels = {
            'skill':'Skill'
        }

class SpecialityForm(ModelForm):
    class Meta:
        model = Speciality
        fields = ['speciality']
        labels = {
            'speciality':'Speciality'
        }


class CertificateForm(ModelForm):
    issuedDate = forms.DateField(widget=DateInput)
    expiryDate = forms.DateField(widget=DateInput)
    class Meta:
        model = Certificate
        fields = ['name' ,'issuingOrg','issuedDate' ,'expiryDate','credentialId' ,'credentialUrl' ,'description']
        labels = {
            'name':'Name',
            'issuingOrg':'Issued Organization',
            'issuedDate': 'Issued On' ,
            'expiryDate':'Expiration Date',
            'credentialId': 'Credential ID' ,
            'credentialUrl': 'Credential Url' ,
            'description':'Description'
        }


class TestimonialForm(ModelForm):
    issuedDate = forms.DateField(widget=DateInput)
    class Meta:
        model = Testimonial
        fields =[ 'attestant' ,'issuedDate' ,'services' , 'designation', 'location' ,'description']
        labels = {
            'attestant':'Attestant' ,
            'issuedDate':'Issued On' ,
            'services':'Services' , 
            'designation':'Designation', 
            'location':'Location' ,
            'description':'Description'
        }

class EducationForm(ModelForm):
    startDate = forms.DateField(widget=DateInput)
    endDate = forms.DateField(widget=DateInput)
    class Meta:
        model = Education
        fields = ['institute', 'degree', 'branch','grade','startDate', 'endDate' ,'description']
        labels = {
            'institute':'Institute', 
            'degree':'Degree', 
            'branch':'Branch',
            'grade':'CGPA/Percentage',
            'startDate':'Start Date', 
            'endDate':'End Date',
            'description':'Description'
        }
