#importing required modules
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User                         #importing User model for authentication
from django.contrib import messages                                 #importing messages to display message when user signups
from django.contrib.auth import authenticate, login, logout
from hackathonProject import settings
from django.core.mail import send_mail 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage,send_mail



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

        # Handling Exceptions in username
        if not username.isalnum():
            messages.error(request, "Username can only contain letters and numbers.")
            return redirect('signup')
        
        # Handling UNIQUE Usernames and Emails
        elif User.objects.filter(username=username):
            messages.error(request, "Username already exist! Try another username.")
            return redirect('signup')
        
        
        elif User.objects.filter(email=email):  
            messages.error(request, "Email already exist! Try another Email.")
            return redirect('signup')
        
        


        # Handling exception in password
        elif password1!=password2:
            messages.error(request,"Enter correct password for confirmation.")
            return redirect('signup')
        
        else:
            # Adding the details of user into User Database Table
            myuser = User.objects.create_user(username, email, password1)
        
            myuser.save()

            messages.success(request,"Your account has been successfully created !!!. We have sent you a confirmation email please confirm by clicking on the activation link provided in the mail.")

        
            

            # ------------------------------------------------ Welcome EMAIL-----------------------------------------------
            subject = "Welcome to DocScheduler"
            message = "Hi" + myuser.username + "!! \n" + "Welcome to DocScheduler!!! \n Thank you for visiting our website. \n\n Thanking You \n DocSchedukler Team"
            from_email= settings.EMAIL_HOST_USER
            to_list= [myuser.email]

            send_mail(subject, message, from_email, to_list, fail_silently= True)
            #------------------------------------------------- Email sent -----------------------------------------------------
            
            return redirect('signin')



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



