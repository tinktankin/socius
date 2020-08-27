from django import forms
from socius.models import memberdirectory

class DirectoryCreationForm(forms.ModelForm):
    class Meta:
        model=memberdirectory
        fields=('DirectoryName','img','Description','MemberLimit','DirectoryId')
        