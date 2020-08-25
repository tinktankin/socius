from django import forms
from .models import Profile,profilePic,Skills,Speciality,Certificate,Testimonial,Education
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName','lastName','email','altEmail','phone','altPhone','address','city','state','country','postalCode','aboutMe']

class ProfilePicForm(ModelForm):
    class Meta:
        model = profilePic
        fields = ['image','status','tagLine']
       
class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

class SpecialityForm(ModelForm):
    class Meta:
        model = Speciality
        fields = ['speciality']

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name' ,'issuingOrg','issuedDate' ,'expiryDate','credentialId' ,'credentialUrl' ,'description']

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields =[ 'attestant' ,'issuedDate' ,'services' , 'designation', 'location' ,'description']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['institute', 'degree', 'branch','grade','startDate', 'endDate' ,'description']



