from django.shortcuts import render, redirect
from .models import Coupon_SU 
from .forms import Coupon_code_SU_
from django.contrib import messages

def create_SU_coupon_(request):

    context = {}
    form_su = Coupon_code_SU_(request.POST)
    if request.method == 'POST':
        if form_su.is_valid():
            form_su.save()
            code = form_su.cleaned_data.get('code')
            messages.success(request, 'Coupon Code is generated successfully!')
            return redirect('SuCoupon') 
    
    else:
        form_su = Coupon_code_SU_()

    context['form_su'] = form_su

    return render(request, 'Coupons/CouponSUGeneration.html', context)


def Coupon_SU_table(request):
    coupons = Coupon_SU.objects.filter(Name = request.user.get_username())
    return render(request, 'Coupons/CouponsSU_table.html', {'coupons':coupons})
