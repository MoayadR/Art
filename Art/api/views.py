from django.shortcuts import render
from Posts.models import Tag
from django.http import JsonResponse
# Create your views here.

def showAllTags(request):
    tags = Tag.objects.all().values()
    tags = list(tags)

    return JsonResponse(tags , safe=False)

