from django.urls import path, include
from userprofile import views as uv

urlpatterns = [
        path('profile', uv.profile, name="profile"),
]