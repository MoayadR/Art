from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile_Data(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE , blank=True)
    gender = models.BooleanField(null=True , blank=False)
    bio = models.TextField(blank = True , null=True)
    profile_pic = models.ImageField(blank=True , default='default.jpeg')

    def __str__(self):
        return self.user.username