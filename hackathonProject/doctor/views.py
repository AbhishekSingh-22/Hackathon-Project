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
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
def doctorhome(request):
    current_user=request.user
    current_username = current_user.username
    print(current_username)
    return render(request, 'doctor/DoctorHomePage.html')
    # return redirect('user/')


def doctordetailform(request):
    return render(request, 'doctor/DoctorDetailForm.html')
    # return redirect('user/')