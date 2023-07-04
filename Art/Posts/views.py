from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm , TagForm
from django.contrib import messages
import PIL

# Create your views here.
@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    context = {'posts' :post}
    return render(request, 'base.html' , context)

@login_required(login_url='login')
def createArt(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            messages.success(request , 'Wrong input, Please Try again...')
            return redirect('create-art')
    # GET method
    form = PostForm()
    context = {'form' : form}
    return render(request , 'Posts/create.html' , context)

@login_required(login_url='login')
def createTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            title = str(form.cleaned_data['title'])
            title = title.lower()
            form.instance.title = title
            form.save()
            return redirect('home')

    # GET Method
    form = TagForm()
    context = {'form':form}
    return render(request , 'Posts/create.html' , context)