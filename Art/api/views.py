from django.shortcuts import render
from Posts.models import Tag
from Access.models import Profile_Data
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from Art.settings import BASE_DIR

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
