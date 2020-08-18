from django.shortcuts import render, redirect
from .models import Destination
from .models import UserList , memberdirectory,DirectoryMembers
from .resources import UserListResource
from django.contrib import messages
from tablib import Dataset 
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.core import mail
from .forms import DirectoryCreationForm
#import uuid 
#from .models import MemberProfile,Phone,Address,Speciality,KeySKills,Certificates,Testimonial,Document,AcademicDetails,Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.

def index(response):
    
    '''dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Vizag'
    dest2.desc = 'The City of Destiny'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'The Silicon City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = True

    dests = [dest1, dest2, dest3]'''

    #dests = Destination.objects.all()

    mems = memberdirectory.objects.all()

    return render(response, "socius/index.html", {'mems': mems})

def Team(request):
    return render(request, "socius/team.html")

@login_required(login_url='login')
def directorypage(request):
    admin=User.objects.filter(is_superuser='True').first()
    return render(request, "socius/directorypage.html",{'admin':admin})



@allowed_users(allowed_roles=['admin','superuser'])
def simple_upload(request):
    if request.method == 'POST':
        user_list = UserListResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'socius/upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        #print(imported_data)
        d=[]
        for data in imported_data:
        	#print(data[1])
            #UserListInvitation(data[2])
            d.append(data[2])
            '''send_mail(
                'MDA Invitation',
                'This is the Invitation of MDA applcation.',
                settings.EMAIL_HOST_USER,
                [data[2]],
                fail_silently=False,
            )'''

            value = UserList(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
                 data[4]
        		)
            value.save()
        l=d
        user=User.objects.filter(is_superuser='True').first()
        current_site = get_current_site(request)
        mail_subject = 'Invite to Socius'
        message = render_to_string('socius/invite.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        for i in l:
            #reciever_list.append(i['email'])
            to_email = i
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        return HttpResponse('Invitations sended')
        '''connection = mail.get_connection()
        connection.open()
        email1 = mail.EmailMessage('MDA Invitation', 'This is the Invitation of MDA applcation.', settings.EMAIL_HOST_USER, d, connection=connection)
        email1.send()
        connection.close()'''

            
            #send_mail('Invitation MDA','This is MDA application Invitation',settings.EMAIL_HOST_USER, data[2], fail_silently=False)
            #send_mail('Invitation MDA', 'This is MDA application Invitation', settings.EMAIL_HOST_USER, data[2], fail_silently=False)
    return render(request, 'socius/upload.html')

    

'''def UserListInvitation(to_email):
    current_site = get_current_site(request)
    mail_subject = 'Invitation MDA.'
    message = render_to_string('accounts/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    #to_email = request.POST['email']
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()'''

def active(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
      #  user.save()
        if user.is_active==True:
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            return redirect('register')
    else:
        return HttpResponse('Invitation link is invalid!')


def create(request,*args,**kwargs):
    if request.method=='POST':
        form=DirectoryCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form=DirectoryCreationForm()
    return render(request,'socius/createdir.html',{'form':form})

def members(response):
   Members=DirectoryMembers.objects.all()
   return render(response, "socius/Members.html",{'Members':Members})
@login_required
def joindirectory(request):
    return render(request,'socius/joindirectory.html')

def joined(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['email']
        Bio=request.POST['bio']
        if DirectoryMembers.objects.filter(Email=Email).exists():
            messages.info(request, 'The email is already registered')
            return redirect('joined')
        else:
            obj2=DirectoryMembers(Name=Name,Email=Email,Bio=Bio)
            obj2.save()
            direcory1=memberdirectory.objects.all()
            return render(request,'socius/directorypage.html')
    else:
        return render(request,'socius/joindirectory.html')


   