
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm

'''
def upload(request):
    return render(request,'documents/upload.html')
'''

def upload(request,*args):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            userdocument = request.user
            fileName = request.POST['fileName']
            uploadFile = request.FILES['uploadFile']
            description = request.POST['description'] 
            obj = Document(fileName=fileName,uploadFile=uploadFile,description=description, user=userdocument)
            obj.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    data = Document.objects.all().filter(user_id=request.user.id).order_by("-uploadedOn")
    context = {
        'form': form,
        'data':data,
    }
    return render(request,'documents/upload.html', context)
