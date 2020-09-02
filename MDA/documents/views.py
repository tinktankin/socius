
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm
from django.views.generic.edit import DeleteView 
import os

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
            #print("uploadfile name :",uploadFile.name)
            #print("uploadfile = ",str(uploadFile)[-3:])
            extension = str(uploadFile) 
            index = extension.rfind('.')
            #print("extension=",extension[index+1:])
            extension = extension[index+1:].lower()
            obj = Document(fileName=fileName,uploadFile=uploadFile,description=description,fileExtension=extension ,user=userdocument)
            obj.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    data = Document.objects.all().filter(user_id=request.user.id).order_by("-uploadedOn")
    #extension = str(Document.objects.all().filter(user_id=request.user.id)[0].uploadFile)[-3:]
    #extension = str(data[uploadFile][-3:])
    ppt_ext = ['ppt','pptx']
    word_ext = ['docx','docm','docb','dotm','dotx']
    excel_ext = ['xlsx','xlsm','xltx','xltm']
    pdf_ext = ['pdf']
    context = {
        'form': form,
        'data':data,
        'ppt_ext': ppt_ext,
        'word_ext':word_ext,
        'excel_ext':excel_ext,
        'pdf_ext': pdf_ext
    }
    return render(request,'documents/upload.html', context)


