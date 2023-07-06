from django.shortcuts import render , redirect
from django.contrib.auth import logout ,login ,authenticate
from .forms import LoginForm , RegisterForm , DataForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password  
from .models import Profile_Data
from django.contrib.auth.decorators import login_required

from Posts.models import Post

# Create your views here.

def loginUser(request):
    if(request.method == 'POST'): #POST Part
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username , password = password)
            if user is not None:
                login(request , user)
                return redirect('home')
            
            #None User
            messages.success(request , 'Wrong credentials please try again..')
            return redirect('login')
        
        # NOT Valid
        messages.success(request , 'Wrong input type please try again ..')
        return redirect('login')
    
    #GET Part
    form = LoginForm()
    context = {'form' : form}
    return render(request , 'Access/login.html' , context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.instance.password = make_password(form.instance.password)
            user = form.save()
            data = Profile_Data(user = user)
            data.save()
            return redirect('login')
        
        # Invalid Form
        messages.success(request , 'Wrong input type please try again ..')
    # GET Method
    form = RegisterForm()
    context = {'form':form}
    return render(request , 'Access/register.html' , context)


def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url = 'login')
def showProfile(request):
    posts = Post.objects.filter(user = request.user)
    return render(request , 'Access/profile.html' , {'posts' : posts})


@login_required(login_url = 'login')
def editProfile(request):
    if request.method == 'POST':
        form = DataForm(request.POST ,request.FILES, instance=request.user.profile_data)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')

    # GET Request
    form = DataForm(instance=request.user.profile_data)
    return render(request , 'Access/edit-profile.html' , {'form' : form})