from django.urls import path
from documents import views


urlpatterns = [
    
    path('upload', views.upload, name="upload"),
    path('dirDisplay',views.dirDisplay,name="dirDisplay"),
]