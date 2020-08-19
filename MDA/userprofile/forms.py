from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, ContactInfo, Skills,Address,Certificate,Testimonial,Education

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','firstName','lastName','bio','tagLine','status']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['email','phone']

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill','speciality']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['flatNo','street','city','state','country','pinCode']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name','issuingOrg','issuedDate','expiryDate','credentialId','credentialUrl','description']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['attestant','issuedDate','services','designation','location','description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institute','degree','branch','grade','startDate','endDate','description']