from django.urls import path, include
from django.contrib import admin
from . import views as v
  
urlpatterns = [ 
    path('user.html', v.profile, name="profile"),
    path('<id>/skillsDel',v.skillsDel,name="skillsDel"),
    path('<id>/specialityDel',v.specialityDel,name="specialityDel"),
    path('<id>/educationDel',v.educationDel,name="educationDel"),
    path('<id>/certicateDel',v.certicateDel,name="certicateDel"),
    path('<id>/testimonialDel',v.testimonialDel,name="testimonialDel"),
    path('<id>/profilePicUpdate', v.profilePicUpdate,name="profilePicUpdate" ),
    path('<id>/profileUpdate', v.profileUpdate,name="profileUpdate" ), 
    path('<id>/skillsUpdate', v.skillsUpdate,name="skillsUpdate" ), 
    path('<id>/specialityUpdate', v.specialityUpdate,name="specialityUpdate" ), 
    path('<id>/educationUpdate', v.educationUpdate,name="educationUpdate" ), 
    path('<id>/certificateUpdate', v.certificateUpdate,name="certificateUpdate" ),
    path('<id>/testimonialUpdate',v.testimonialUpdate,name="testimonialUpdate")
] 
'''
urlpatterns = [
        #path('admin/', admin.site.urls),
        path('profile', views.profile,name="profile"), 
        path('dummy',views.dummy,name="dummy")
]
'''