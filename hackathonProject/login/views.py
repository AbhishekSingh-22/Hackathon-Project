#importing required modules
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User                         #importing User model for authentication
from django.contrib import messages                                 #importing messages to display message when user signups
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    
    # Storing details from form to User table
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password"]
        password2=request.POST["confirmPass"]

        if password1==password2:
            myuser = User.objects.create_user(username, email, password1)
        
            myuser.save()

            messages.success(request,"Your account has been successfully created !!!")

            return redirect('signin')
        else:
            messages.error(request,"Enter correct password for confirmation.")


    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username, password=password)         
        #this will return a not none value is the user is authenticate otherwise it returns none if the user have entered the wrong credentials"""

        if user is not None:
            login(request, user)
            messages.success(request,"Logged in !")
            return render(request, 'authentication/index.html', {'name': username})
            

        else:
            messages.error(request, "Wrong Credentials")

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You are successfully logged out")

    return redirect('home')


