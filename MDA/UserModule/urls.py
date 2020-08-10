from django.urls import path
from . import views

urlpatterns = [
    path('',views.Profile,name='Profile'),
    path('Profile.html',views.Profile, name='Profile'),
    path('PersonalDetails.html/',views.PersonalDetails,name='PersonalDetails'),
    path('Education.html/',views.Education,name='Education'),
    path('Skills.html/',views.Skills,name='Skills'),
    path('Certifications.html/',views.Certifications,name='Certifications'),
    path('Testimonials.html',views.Testimonials,name='Testimonials'),
]