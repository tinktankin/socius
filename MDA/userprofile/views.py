from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import profileForm
from .models import profile

@login_required
def profileView(request):
    if request.method == 'POST':
        profile_form = profileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        profile_form = profileForm()
    context = {'profile_form':profile_form}
    return render(request,'profile.html',context)


#@login_required
def contactInfoView(request):
    if request.method == 'POST':
        contactInfo_form = contactInfoForm(request.POST)
        if contactInfo_form.is_valid():
            contactInfo_form.save()
            messages.success(request,('Your contact details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        contactInfo_form = contactInfoForm()
    
    context = {'contactInfo_form':contactInfo_form}
    return render(request,'contactInfo.html',context)


#@login_required
def addressView(request):
    if request.method == 'POST':
        address_form = addressForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            messages.success(request,('Your addresss details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        address_form = addressForm()
    
    context = {'address_form':address_form}
    return render(request,'address.html',context)


#@login_required
def skillsView(request):
    ''''
    template_name = 'skills.html'

    def get(self,request):
        form = skillsForm()
        skill = skills.objects.all()
        args = {'form':form,'skill':skill}
        return render(request, self.template_name,args)
    '''
    if request.method == 'POST':
        skills_form = skillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            messages.success(request,('Your skills updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        skills_form = skillsForm()
    
    context = {'skills_form':skills_form}
    return render(request,'skills.html',context)


#@login_required
def certificateView(request):
    if request.method == 'POST':
        certificate_form = certificateForm(request.POST)
        if certificate_form.is_valid():
            certificate_form.save()
            messages.success(request,('Your  certifications updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        certificate_form = skillsForm()
    
    context = {'certificate_form':certificate_form}
    return render(request,'certificate.html',context)


#@login_required
def testimonialView(request):
    if request.method == 'POST':
        testimonial_form = testimonialForm(request.POST)
        if testimonial_form.is_valid():
            testimonial_form.save()
            messages.success(request,('Your testimonials updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        testimonial_form = testimonialForm()
    
    context = {'testimonial_form':testimonial_form}
    return render(request,'testimonial.html',context)


#@login_required
def educationView(request):
    if request.method == 'POST':
        education_form = educationForm(request.POST)
        if education_form.is_valid():
            education_form.save()
            messages.success(request,('Your academic details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        education_form = educationForm()
    
    context = {'education_form':education_form}
    return render(request,'education.html',context)
'''
@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_Form = profileForm(request.POST, instance=request.user)
        if profile_Form.is_valid():
            profile_Form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_Form = profileForm(instance=request.user)
    return render(request, 'profiles/profile.html', {
        'profile_Form': profile_Form
    })
'''