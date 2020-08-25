from django.urls import path, include
from django.contrib import admin
from userprofile1 import views

urlpatterns = [
        #path('admin/', admin.site.urls),
        path('profile', views.profile,name="profile"), 
        path('dummy',views.dummy,name="dummy")
]