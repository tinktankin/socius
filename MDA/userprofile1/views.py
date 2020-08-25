from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,profilePic,Skills,Speciality,Certificate,Testimonial,Education
from django.shortcuts import (get_object_or_404, 
							render, 
							HttpResponseRedirect) 
from .forms import ProfileForm
def dummy(request):
    return render(request,'dummy.html')




def profile(request,*args):
    print("in profile method")
    if request.method == 'POST':
        p_form = ProfileForm(request.POST) 
        if p_form.is_valid():
            print("data entry")
            user = request.user
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            altEmail = request.POST['altEmail']
            phone = request.POST['phone']
            altPhone = request.POST['altPhone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            postalCode = request.POST['postalCode']

            aboutMe = request.POST['aboutMe']

            obj = Profile(firstName=firstName, lastName=lastName,email=email,altEmail=altEmail,phone=phone,altPhone=altPhone,address=address,city=city,state=state,country=country,postalCode=postalCode,aboutMe=aboutMe,user=user)
            obj.save()
            messages.success(request, f'Your skills has been updated!')
            return redirect('profile')

    else:
        p_form = ProfileForm(instance=request.user)
    p_data = Profile.objects.all().filter(user_id=request.user.id)
    
    context = {
        'p_form': p_form,
        'p_data': p_data
    }
    return render(request, 'profile.html', context)

