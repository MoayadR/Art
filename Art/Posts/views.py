from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {'posts' :post}
    return render(request, 'base.html' , context)