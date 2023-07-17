from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Post , Tag , Comment
from .forms import PostForm , TagForm
from django.contrib import messages
import PIL
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def home(request):
    searchTags = request.GET.get('search')
    if searchTags:
        tagsSet = Tag.objects.filter(title = searchTags)
        post = Post.objects.filter(tags__in = tagsSet)     
    else:
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
    return render(request , 'Posts/create-post.html' , context)

@login_required(login_url='login')
def createTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            title = str(form.cleaned_data['title'])
            title = title.lower()
            
            checkObject = Tag.objects.filter(title = title)
            if checkObject.exists():
                return redirect('home')

            form.instance.title = title
            form.save()
            return redirect('home')

    # GET Method
    form = TagForm()
    context = {'form':form}
    return render(request , 'Posts/create-tag.html' , context)


@login_required(login_url='login')
def viewProfile(request , id):
    user = User.objects.get(id = id)

    if user:
        posts = Post.objects.filter(user = user)
        return render(request , 'Posts/view-profile.html' , {'posts':posts , 'user':user})
    
    #Else
    messages.success(request, 'This user doesn\'t exist')
    return render('home')

@login_required(login_url='login')
def viewArt(request , id):
    artItem = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = artItem)
    if artItem:
        posts =Post.objects.filter(tags__in = artItem.tags.all()).exclude(art = artItem.art)
        return render(request , 'Posts/view-art.html' , {'posts':posts , 'art':artItem , 'comments':comments})

    # Else
    messages.success(request, 'This Art doesn\'t exist')
    return render('home')