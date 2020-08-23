from django.db import models
'''from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField(default='')
    tagline = models.TextField(default='')
    status = models.TextField(default='')


    def __str__(self):
        return self.user.username'''