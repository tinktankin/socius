from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileForm, ContactForm, SkillsForm,AddressForm,CertificateForm,TestimonialForm,EducationForm
from .models import Profile, Skills, ContactInfo , Address,Certificate, Testimonial, Education

def onlineprofile(request):
    return render(request,'onlineprofile.html')
'''
This is with signals
@login_required
def profile(request):
    print("Entered profile function")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)
'''

@login_required
def profile(request,*args):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST,request.FILES,instance=request.user) 
  
        if p_form.is_valid():
            user = User.objects.filter().first()
            #image = request.POST['image']
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            aboutMe = request.POST['aboutMe']
            tagLine = request.POST['tagLine']
            status = request.POST['status']
            obj = Profile(firstName=firstName, lastName=lastName,aboutMe=aboutMe,tagLine=tagLine,status=status,user=user)
            obj.save()
            messages.success(request, f'Your skills has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileForm(instance=request.user)
    #s_data = Skills.objects.all().select_related('userSkills')
    context = {
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


@login_required
def skills(request,*args):
    print("Entered skills function")
    if request.method == 'POST':
        s_form = SkillsForm(request.POST,instance=request.user)
        if s_form.is_valid():
            userSkills = User.objects.filter().first()
            skill = request.POST['skill']
            speciality = request.POST['speciality']
            obj = Skills(skill=skill,speciality=speciality,userSkills=userSkills)
            obj.save()
            messages.success(request, f'Your skills has been updated!')
            return redirect('skills')

    else:
        s_form = SkillsForm(instance=request.user)
    s_data = Skills.objects.all().select_related('userSkills')
    context = {
        's_form': s_form,
        's_data': s_data
    }
    return render(request, 'skills.html', context)



@login_required
def contact(request,*args):
    if request.method == 'POST':
        c_form = ContactForm(request.POST,instance=request.user)
        if c_form.is_valid():
            userContact = User.objects.filter().first()
            email = request.POST['email']
            phone = request.POST['phone']
            obj = ContactInfo(email=email,phone=phone,userContact=userContact)
            obj.save()
            messages.success(request, f'Your contact details has been updated!')
            return redirect('profile')

    else:
        c_form = ContactForm(instance=request.user)
    context = {
        'c_form': c_form,
    }
    return render(request, 'profile.html', context)




@login_required
def address(request,*args):
    if request.method == 'POST':
        a_form = AddressForm(request.POST,instance=request.user)
        if a_form.is_valid():
            userAddress = User.objects.filter().first()
            flatNo = request.POST['flatNo']
            street = request.POST['street']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            pinCode = request.POST['pinCode']
            obj = Address(flatNo=flatNo,street=street,city=city,state=state,country=country,pinCode=pinCode,userAddress=userAddress)
            obj.save()
            messages.success(request, f'Your contact details has been updated!')
            return redirect('profile')

    else:
        a_form = AddressForm(instance=request.user)
    context = {
        'a_form': a_form,
    }
    return render(request, 'profile.html', context)


@login_required
def certificate(request,*args):
    if request.method == 'POST':
        cer_form =CertificateForm(request.POST,instance=request.user)
        if cer_form.is_valid():
            userCertificate = User.objects.filter().first()
            name = request.POST['name']
            issuingOrg = request.POST['issuingOrg']
            issuedDate = request.POST['issuedDate']
            expiryDate = request.POST['expiryDate']
            credentialId = request.POST['credentialId']
            credentialUrl = request.POST['credentialUrl']
            description = request.POST['description']
            obj = Certificate(name=name,issuingOrg=issuingOrg,issuedDate=issuedDate,expiryDate=expiryDate,credentialId=credentialId,credentialUrl=credentialUrl,description=description,userCertificate=userCertificate)
            obj.save()
            messages.success(request, f'Your contact details has been updated!')
            return redirect('profile')

    else:
        cer_form =CertificateForm (instance=request.user)
    context = {
        'cer_form': cer_form,
    }
    return render(request, 'profile.html', context)



@login_required
def testimonial(request,*args):
    if request.method == 'POST':
        t_form = TestimonialForm(request.POST,instance=request.user)
        if t_form.is_valid():
            userTestimonial = User.objects.filter().first()
            attestant = request.POST['attestant']
            issuedDate = request.POST['issuedDate']
            services = request.POST['services']
            designation = request.POST['designation']
            location = request.POST['location']
            description = request.POST['description']
            obj = Testimonial(attestant=attestant, issuedDate=issuedDate, services=services,designation=designation,location=location,description=description,userTestimonial=userTestimonial)
            obj.save()
            messages.success(request, f'Your Testimonials has been updated!')
            return redirect('profile')

    else:
        t_form = TestimonialForm(instance=request.user)
    context = {
        't_form': t_form,
    }
    return render(request, 'profile.html', context)


@login_required
def education(request,*args):
    if request.method == 'POST':
        e_form = EducationForm(request.POST,instance=request.user)
        if e_form.is_valid():
            userEducation = User.objects.filter().first()
            institute = request.POST['institute']
            degree = request.POST['degree']
            branch = request.POST['branch']
            grade = request.POST['grade']
            startDate = request.POST['startDate']
            endDate = request.POST['endDate']
            description = request.POST['description']
            obj = Education(institute=institute,degree=degree,branch=branch,grade=grade,startDate=startDate,endDate=endDate,description=description,userEducation=userEducation)
            obj.save()
            messages.success(request, f'Your education details has been updated!')
            return redirect('profile')

    else:
        e_form = EducationForm(instance=request.user)
    context = {
        'e_form': e_form,
    }
    return render(request, 'profile.html', context)
