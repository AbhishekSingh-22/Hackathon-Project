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
from doctor.models import doctordetail
from patient.models import patientform



# Create your views here.
def home(request):

    # patient_detail = patientform()
    if not patientform.objects.filter(fname=request.user.first_name) :
        patient_detail=patientform(pusername=request.user.username, fname=request.user.first_name, lname=request.user.last_name, pemail=request.user.email)

        patient_detail.save()

        

    doctorTable = doctordetail.objects.all()

    params={}
    params['doctorTable']=doctorTable



    return render(request, 'patient/home.html',params)

def form(request):

    particular_patient=patientform.objects.filter(pusername= request.user.username)[0]

    if request.method == "POST":

        #Extracting values from form
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        bloodgrp = request.POST.get("bloodgrp")
        gender = request.POST.get("gender")
        email = request.POST.get("email")

        contact = request.POST.get("contact")
        
        state = request.POST.get("state")
        
        allergy = request.POST.get("allergy")
        
        medications = request.POST.get("medications")
        
        insurance = request.POST.get("insurance")
        
        drughistory = request.POST.get("drughistory")
        symptoms = request.POST.get("symptoms")
        medicalhistory = request.POST.get("medicalhistory")

        #Updating values in model
        particular_patient.age = age
        particular_patient.height = height
        particular_patient.weight = weight
        particular_patient.bloodgrp = bloodgrp
        particular_patient.gender = gender
        particular_patient.contact = contact
        particular_patient.state = state
        particular_patient.allergy = allergy
        particular_patient.goingonMedications = medications
        particular_patient.insurance = insurance
        particular_patient.drughistory = drughistory
        particular_patient.symptoms = symptoms
        particular_patient.medicalhistory = medicalhistory


        particular_patient.save()

        return redirect("home")
    

    params={
        "fname": particular_patient.fname,
        "lname": particular_patient.lname,
        "age": particular_patient.age,
        "height": particular_patient.height,
        "weight": particular_patient.weight,
        "bloodgrp": particular_patient.bloodgrp,
        "gender": particular_patient.gender,
        "email": particular_patient.pemail,

        "contact": particular_patient.contact,
        
        "state": particular_patient.state,
        
        "allergy": particular_patient.allergy,
        
        "medications": particular_patient.goingonMedications,
        
        "insurance": particular_patient.insurance,
        
        "drughistory": particular_patient.drughistory,
        "symptoms": particular_patient.symptoms,
        "medicalhistory": particular_patient.medicalhistory
        
    }

    return render(request, 'patient/form.html', params)