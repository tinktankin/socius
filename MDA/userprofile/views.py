from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, ContactForm, SkillsForm
from .models import Profile, Skills, ContactInfo , Address,Certificate, Testimonial, Education

@login_required
def profile(request):
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

@login_required
def skills(request,*args):
    if request.method == 'POST':
        s_form = SkillsForm(request.POST,instance=request.user)
        if s_form.is_valid():
            user = User.objects.filter().first()
            skill = request.POST['skill']
            speciality = request.POST['speciality']
            obj = Skills(skill=skill,speciality=speciality,user=user)
            obj.save()
            messages.success(request, f'Your skills has been updated!')
            return redirect('skills')

    else:
        s_form = SkillsForm(instance=request.user)
    context = {
        's_form': s_form,
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
            return redirect('contact')

    else:
        c_form = ContactForm(instance=request.user)
    context = {
        'c_form': c_form,
    }
    return render(request, 'contact.html', context)




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
            return redirect('contact')

    else:
        a_form = AddressForm(instance=request.user)
    context = {
        'a_form': a_form,
    }
    return render(request, 'contact.html', context)
