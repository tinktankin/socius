from django.urls import path, include
from userprofile import views as uv

urlpatterns = [
        path('profile', uv.profile, name="profile"),
        path('profile',uv.contact,name='contact'),
        path('profile',uv.skills,name='skills'),
        path('profile',uv.education,name='education'),
        path('onlineprofile',uv.onlineprofile,name='onlineprofile')
]