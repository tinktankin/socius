from django import forms
from socius.models import memberdirectory

class DirectoryCreationForm(forms.ModelForm):
    class Meta:
        model=memberdirectory
        fields=('name','img','desc','size')
        