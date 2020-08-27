from django.urls import path, include
from django.contrib import admin
from . import views as v
  
urlpatterns = [ 
    path('profile', v.profile, name="profile"), 
    path('<id>/profileUpdate', v.profileUpdate,name="profileUpdate" ), 
    path('<id>/profilePicUpdate', v.profilePicUpdate,name="profilePicUpdate" ), 
    path('<id>/skillsUpdate', v.skillsUpdate,name="skillsUpdate" ), 
    path('<id>/specialityUpdate', v.specialityUpdate,name="specialityUpdate" ), 
    path('<id>/educationUpdate', v.educationUpdate,name="educationUpdate" ), 
    path('<id>/certificateUpdate', v.certificateUpdate,name="certificateUpdate" ),
    path('<id>/testimonialUpdate',v.testimonialUpdate,name="testimonialUpdate")
] 