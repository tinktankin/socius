from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    firstName = models.CharField(max_length=20,blank=True,default='')
    lastName = models.CharField(max_length=20,blank=True,default='')
    bio = models.TextField(default='', blank=True)
    tagLine = models.TextField(blank=True,default='')
    #profileStatus = models.IntegerField(default=0) #to know how much profile does the user completed
    status = models.TextField(blank=True,default='')
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

