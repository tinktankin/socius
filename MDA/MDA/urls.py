"""MDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from socius import views as v
from userprofile1 import views as uv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('userprofile1.urls')),
    path('profile.html',uv.profile,name="profile"),
    path('admin/', admin.site.urls),
    path('', v.index1, name="index1"),
    path('index1.html', v.index1, name="index1"),
    path('loggedin.html', v.loggedin, name="loggedin"),
    path('user.html', v.user, name="user"),
    path('dashboard.html', v.dashboard, name="dashboard"),
    path('dummy.html', v.dummy, name="dummy"),
    path('directorypage.html', v.directorypage, name="directorypage"),
    path('team.html', v.Team, name="team"),
    path('create', v.create, name="create"),
    path('members',v.members,name="members"),
    path('joined',v.joined,name="joined"),
    path('joindirectory',v.joindirectory,name="joindirectory"),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('adduser/',v.simple_upload,name='simple_upload'),
    path('active/<uidb64>/<token>/',v.active, name='active'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
