from django.shortcuts import render
from django.http import HttpResponse
from Posts.models import Tag
from Access.models import Profile_Data
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from Posts.models import Comment , Post
from django.views.decorators.csrf import csrf_exempt

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

    return HttpResponse("Created Comment Successfully")


def getUserLove(request , postID):
    post = Post.objects.get(id = postID )
    response = {"status" : False}
    if request.user in post.love.all():
        response["status"] = True
        
    return JsonResponse(response)

def addUserLove(request , postID):
    post = Post.objects.get(id = postID )
    post.love.add(request.user)
    return JsonResponse({"status":"Added Love"})

def removeUserLove(request , postID):
    post = Post.objects.get(id = postID )
    post.love.remove(request.user)
    return JsonResponse({"status":"Removed Love"})

@csrf_exempt
def banUser(request):
    # make a banned model for user
    if request.user.is_superuser == True or request.user.is_staff == True:
        data = json.loads(request.body)
        object = User.objects.get(id = data['id'])
        object.is_active = False
        object.save()
        return HttpResponse("Banned Successfully")