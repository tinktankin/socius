# forms.py
from django import forms
from multi_email_field.forms import MultiEmailField
from django.contrib.auth.models import User
from .models import profile

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('photo','firstName','lastName','bio','tagLine','status')

