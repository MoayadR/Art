from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    context = {'posts' :post}
    return render(request, 'base.html' , context)