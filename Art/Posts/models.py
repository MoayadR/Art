from django.db import models
from django.contrib.auth.models import User
import PIL

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True , blank= True)
    tags = models.ManyToManyField(Tag)
    love = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    art = models.ImageField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.TextField(blank= False , null = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
