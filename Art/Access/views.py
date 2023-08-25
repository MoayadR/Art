from django.shortcuts import render , redirect
from django.contrib.auth import logout ,login ,authenticate
from .forms import LoginForm , RegisterForm , DataForm  
from django.contrib import messages
from django.contrib.auth.hashers import make_password  
from .models import Profile_Data
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .tokens import account_activation_token

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
            if user != None and user.is_active == False:
                messages.success(request , 'Please Activate your account first.')
                return redirect('login')
            messages.success(request , 'Wrong credentials please try again..')
            return redirect('login')
        
        # NOT Valid
        messages.success(request , 'Wrong input type please try again ..')
        return redirect('login')
    
    #GET Part
    form = LoginForm()
    context = {'form' : form}
    return render(request , 'Access/login.html' , context)



def sendMail(subject , message , recipientList):
    #kzsowcjyccdkekmf
    emailFrom = settings.EMAIL_HOST_USER
    send_mail(subject , message , emailFrom , recipientList)
    


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.instance.password = make_password(form.instance.password)
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            messages.success(request , "An Email was Sent to Validate your Account.")
            #email sending 
            subject = "Email Confirmation"
            message = render_to_string('Access/email.html' , {'username': user.username  , "validationLink" :"http://127.0.0.1:8000/auth/activate/" +urlsafe_base64_encode(force_bytes(user.pk)) + '/' + account_activation_token.make_token(user)})
            recipientList = [user.email]
            sendMail(subject , message , recipientList )

            data = Profile_Data(user = user)
            data.save()
            login(request , user)
            return redirect('create-profile' , userID = user.id)
        
        # Invalid Form
        messages.success(request , 'Wrong input type please try again ..')
    # GET Method
    form = RegisterForm()
    context = {'form':form}
    return render(request , 'Access/register.html' , context)


def activate(request , uidb64 , token):
    try:
        user = User.objects.get(id = force_str(urlsafe_base64_decode(uidb64)))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user != None and account_activation_token.check_token(user , token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
    else:
        messages.success(request , "Activation Link is Invalid")
    return redirect('login')
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url = 'login')
def showProfile(request):
    posts = Post.objects.filter(user = request.user)
    return render(request , 'Access/profile.html' , {'posts' : posts})

def createProfile(request , userID):
    user = User.objects.get(id = userID)

    if request.method == 'POST':
        form = DataForm(request.POST , request.FILES , instance=user.profile_data)
        if form.is_valid():
           form.instance.user = user
           form.save()
           return redirect('home')
    #GET method
    form = DataForm(instance=user.profile_data)
    return render(request , 'Access/edit-profile.html' , {'form' : form})


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

@login_required(login_url = 'login')
def editAccount(request):
    return render(request , 'Access/edit-account.html')

@login_required(login_url = 'login')
def editFirstName(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        user = request.user
        user.first_name = firstName
        user.save()
        return redirect('edit-account')

    return render(request , 'Access/editFirstName.html')

@login_required(login_url = 'login')
def editLastName(request):
    if request.method == 'POST':
        lastName = request.POST['last_name']
        user = request.user
        user.last_name = lastName
        user.save()
        return redirect('edit-account')

    return render(request , 'Access/editLastName.html')

@login_required(login_url = 'login')
def editEmail(request):
    if request.method == 'POST':
        Email = request.POST['email']
        user = request.user
        user.email = Email
        user.save()
        return redirect('edit-account')

    return render(request , 'Access/editEmail.html')


@login_required(login_url = 'login')
def editPassword(request):
    if request.method == 'POST':
        inputPassword = request.POST['password']
        inputRePassword = request.POST['re-password']
        if inputPassword == inputRePassword:
            inputPassword = make_password(inputPassword)
            user = request.user
            user.password = inputPassword
            user.save()
            return redirect('edit-account')
           
        #else
        messages.success(request,'The Two Passwords don\'t match')
        return redirect('edit-account')

    return render(request , 'Access/editPassword.html')