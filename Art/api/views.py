from django.shortcuts import render
from django.http import HttpResponse
from Posts.models import Tag
from Access.models import Profile_Data
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from Posts.models import Comment

import simplejson as json

# Create your views here.

def showAllTags(request):
    tags = Tag.objects.all().values()
    tags = list(tags)

    return JsonResponse(tags , safe=False)


def showMyID(request):
    user = serializers.serialize("python",[request.user] ,  fields=('pk'))
    return JsonResponse(user , safe=False)

def showMyProfileData(request , id):
    user = User.objects.get(id = id)
    data = Profile_Data.objects.get(user = user)
    data = serializers.serialize("python" , [data])
    return JsonResponse(data , safe=False)

def createComment(request):
    content = json.loads(request.body)
    user = request.user
    commentText = content["text"]
    postId = content["postID"]
    
    Comment.objects.create(text = commentText , user = user , post_id =postId )

    return HttpResponse("Oh yeah")