from django.shortcuts import render, redirect
from .models import *
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

def blog(request):
    return render(request,'socius/blog.html')






def index1(response):
    
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

    return render(response, "socius/index1.html", {'mems': mems})

'''def index(request):
    return render(request, "socius/index.html")'''

def loggedin(request):
    id=request.user.id
    user1=memberdirectory.objects.filter(user_id=id).first()
    user2=DirectoryMembers.objects.filter(user_id=id).first()
    if(user1 is not None)and(user2 is None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'dir':dir})
    elif (user1 is None)and(user2 is not None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'mydir':mydir})
    elif (user1 is not None)and(user2 is not None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'mydir':mydir,'dir':dir})

    else:
        return render(request,'socius/dashboard1.html')

'''def user(request):
    return render(request,"socius/user.html")'''

def dashboard(request):
    id=request.user.id
    user1=memberdirectory.objects.filter(user_id=id).first()
    user2=DirectoryMembers.objects.filter(user_id=id).first()
    if(user1 is not None)and(user2 is None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'dir':dir})
    elif (user1 is None)and(user2 is not None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'mydir':mydir})
    elif (user1 is not None)and(user2 is not None):
        l=[]
        id=request.user.id
        dir=memberdirectory.objects.filter(user_id=id).all()
        mydir1=DirectoryMembers.objects.filter(user_id=id).values('DirectoryId')
        for i in mydir1:
            l.append(i['DirectoryId'])
        print(l)
        for j in l:
            mydir=memberdirectory.objects.filter(DirectoryId=j).all()
        return render(request,'socius/dashboard.html',{'mydir':mydir,'dir':dir})

    else:
        return render(request,'socius/dashboard1.html')

def Team(request):
    return render(request, "socius/team.html")

def About(request):
    return render(request,"socius/about.html")

def contact(request):
    return render(request,"socius/contact.html")

@login_required(login_url='login')
def directorypage(request):
    if request.method=='POST':
        SuperUser=User.objects.filter(is_staff=True).first
        directoryid=request.POST['DirectoryId']
        members=DirectoryMembers.objects.filter(DirectoryId=directoryid)
        
        #admin=User.objects.filter(is_superuser='True').first()
        return render(request,'socius/directorypage.html',{'members':members,'SuperUser':SuperUser})
    else:
        return redirect('dashboard')



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
            id=request.user.id
            user=User.objects.filter(id=id).first()
            DirectoryName=request.POST['DirectoryName']
            Description=request.POST['Description']
            img=request.FILES['img']
            DirectoryId=request.POST['DirectoryId']
            MemberLimit=request.POST['MemberLimit']
            obj1=memberdirectory(DirectoryName=DirectoryName,Description=Description,DirectoryId=DirectoryId,MemberLimit=MemberLimit,img=img,user=user)
            obj1.save()
            return redirect('dashboard')
    else:
        form=DirectoryCreationForm()
    return render(request,'socius/createdir.html',{'form':form})

def members(response):
    Members=DirectoryMembers.objects.filter()
    return render(response, "socius/Members.html",{'Members':Members})

def dummy(response):
    DirectoryId = DirectorymembersDirectory.objects.filter(memberdirectory_id=9)
    print(DirectoryId)


@login_required
def joindirectory(request):
    return render(request,'socius/joindirectory1.html')

def joined(request):
    if request.method=='POST':
        user=request.user.id
        Name=request.POST['Name']
        Email=request.POST['email']
        Bio=request.POST['bio']
        #user = request.user 
        DirectoryId=request.POST['DirectoryId']
        if DirectoryMembers.objects.filter(Email=Email).exists():
            messages.info(request, 'The email is already registered')
            return redirect('joined')
        else:
            obj2=DirectoryMembers(Name=Name,Email=Email,Bio=Bio,DirectoryId=DirectoryId,user_id=user)
            #obj3=DirectoryMemberTable(memdirectory=memberdirectory_id,directorymems=user)
            obj2.save()
            #obj3.save()
            #obj2.memberdirectory.add(obj1)
            return render(request,'socius/dashboard.html')
    else:
        return render(request,'socius/joindirectory.html')

def alldirectories(request):
    user1 = request.user 
    mems=memberdirectory.objects.exclude(user_id=user1)
    return render(request,'socius/alldirectories.html', {'mems': mems})
   