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
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

from .models import doctordetail, slot_table                   # Importing doctordetail table/model
from patient.models import datewise_slot, booking, patientform


# Create your views here.
def doctorhome(request):
    doctor_detail=doctordetail()

    if doctordetail.objects.filter(dusername=request.user.username):

        doc_bookings = booking.objects.filter(doctor = request.user.username, status = "Unapproved")

        params={
            "doc_bookings" : doc_bookings
        }

        

        return render(request, 'doctor/DoctorHomePage.html',params)
    
    else:
       
        
        doctor_detail= doctordetail(dusername = request.user.username, fname = request.user.first_name, lname = request.user.last_name, email = request.user.email)
        # doctor_detail.duser = request.user
        # doctor_detail.dusername = request.user.username
        # doctor_detail.fname = request.user.first_name
        # doctor_detail.lname = request.user.last_name
        # doctor_detail.email = request.user.email
        doctor_detail.save()


        return redirect("doctordetailform")

# def update_viemoreTable(request):


def viewmore(request):
    if request.method == "POST":
        patientusername = request.POST.get("patientusername")
        pfname = request.POST.get("fname")
        plname = request.POST.get("lname")
       
        patientdetail = patientform.objects.filter(pusername = patientusername, fname = pfname, lname = plname)[0]
        params={
        "fname": patientdetail.fname,
        "lname": patientdetail.lname,
        "age": patientdetail.age,
        "height": patientdetail.height,
        "weight": patientdetail.weight,
        "bloodgrp": patientdetail.bloodgrp,
        "gender": patientdetail.gender,
        "email": patientdetail.pemail,

        "contact": patientdetail.contact,
        
        "state": patientdetail.state,
        
        "allergy": patientdetail.allergy,
        
        "medications": patientdetail.goingonMedications,
        
        "insurance": patientdetail.insurance,
        
        "drughistory": patientdetail.drughistory,
        "symptoms": patientdetail.symptoms,
        "medicalhistory": patientdetail.medicalhistory
        
        }

        return render(request, "doctor/PatientDetail.html", params)
        
def updateapprove(request):
    if request.method == "POST":
        bid = request.POST.get("bookingid")
        pusername = request.POST.get("patientusername")
        pfname = request.POST.get("pfname")
        slot = request.POST.get("slot")
        dusername = request.POST.get("dusername")
        slotNum = request.POST.get("slotNum")

        booking_instance = booking.objects.filter( bookingid = bid, pusername = pusername, pfname= pfname, slot = slot, doctor = dusername, slotNum = slotNum)[0]

        booking_instance.status = "Approved"

        booking_instance.save()

        return redirect("doctorhome")




def doctordetailform(request):
    particular_doc=doctordetail.objects.filter(dusername= request.user.username)[0]
    if request.method=="POST":
        
        # Extracting values from form
        # fname=request.POST.get("fname")
        
        contact =request.POST.get("contact")
        image=request.FILES.get("image")
        specialization=request.POST.get("specialization")
        specdegree=request.FILES.get("specdegree")
        license=request.FILES.get("license")
        desc=request.POST.get("desc")
        fromtime=request.POST.get("fromtime")
        totime=request.POST.get("totime")
        eveningfromtime=request.POST.get("eveningfromtime")
        eveningtotime=request.POST.get("eveningtotime")
        avgtime=request.POST.get("avgtime")
        housenum=request.POST.get("housenum")
        hcity=request.POST.get("hcity")
        hlandmark=request.POST.get("hlandmark")
        hzip=request.POST.get("hzip")
        hstate=request.POST.get("hstate")
        clocation=request.POST.get("clocation")
        ccity =request.POST.get("ccity")
        czip=request.POST.get("czip")
        cstate=request.POST.get("cstate")

        #----------------- updating values in doctorForm==================

        #Assigning Dr. tag to fname
        firstName= request.user.first_name
        if 'Dr.'.upper() in firstName:
            particular_doc.fname=firstName

        else:
            firstName= 'Dr. '+ firstName
            particular_doc.fname=firstName

            
        particular_doc.contact = contact

        # managaing Image file
        if image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_path = fs.save('doctor/images/' + image.name, ContentFile(image.read()))
            particular_doc.image = image



        particular_doc.specialization = specialization

        # Managing Files
        if specdegree:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_path = fs.save('doctor/files/' + specdegree.name, specdegree)
            particular_doc.specdegree = specdegree

        if license:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_path = fs.save('doctor/files/' + license.name, license)

            particular_doc.license = license

        particular_doc.desc = desc
        particular_doc.fromtime = fromtime
        particular_doc.totime = totime
        particular_doc.eveningfromtime = eveningfromtime
        particular_doc.eveningtotime = eveningtotime
        particular_doc.avgtime = avgtime
        particular_doc.housenum = housenum
        particular_doc.hcity = hcity
        particular_doc.hlandmark = hlandmark
        particular_doc.hzip = hzip
        particular_doc.hstate = hstate
        particular_doc.clocation = clocation
        particular_doc.ccity = ccity
        particular_doc.czip = czip
        particular_doc.cstate = cstate

        
        particular_doc.save()


            ####---------------------------------- Slot calculation----------------------------------#####
    
        # Extracting time in string
        fromhrs, frommin = fromtime.split(':')
        tohrs, tomin = totime.split(':')

        # Converting time to int
        # fromhrs = int(fromhrs)
        # frommin = int(frommin)
        # tohrs = int(tohrs)
        # tomin = int(tomin)

        # Storing avg time in int format
        avgtime = int(avgtime)
        
        totalmins= (abs(int(fromhrs)- int(tohrs))*60 )+ abs(int(frommin)-int(tomin))
        Totalslots = totalmins//avgtime

        slot=[str(fromhrs)+':'+str(frommin)]

        for i in range(1,Totalslots+1):
            fromhrs, frommin=slot[i-1].split(':')
            if int(frommin)+avgtime < 60:

                addedmins = int(frommin)+avgtime
                createdSlot =(fromhrs +':'+str(addedmins))
                slot.append(createdSlot)
            
            elif int(frommin)+avgtime ==  60:
                addedhrs = (int(fromhrs)+1)
                addedhrs = str(addedhrs)
                if len(addedhrs)==1:
                    addedhrs = '0'+addedhrs
                createdSlot = addedhrs+':'+'00'
                slot.append(createdSlot)


            else:
                remaining_mins = abs(60 - (int(frommin)+avgtime))
                addedhrs = (int(fromhrs)+1)
                addedhrs = str(addedhrs)
                if len(addedhrs)==1:
                    addedhrs = '0'+addedhrs
                createdSlot = addedhrs+':'+ str(remaining_mins)
                slot.append(createdSlot)

        print(slot)

        SLOT = {}
        slot_countList = []
        start = 0
        hour = (slot[0][0:2])    
        hour = int(hour)
        total_hrs = 0
        for j in range(len(slot)):
            if int(slot[j][0:2]) == hour + 1:       
                slotcount = abs(start - (j))
                start= j
                
                if len(slot[j][0:2]) == 1:
                    time = ("0"+str(hour)+":00") +" -> "+ ("0"+str(hour+1)+":00")
                    SLOT[time]=slotcount

                else:
                    time = (str(hour)+":00") +" -> "+ (str(hour+1)+":00")
                    SLOT[time]=slotcount


                hour = hour +1
                total_hrs = total_hrs+1
        
        print(SLOT)
                    
                    
                    ####---------------------------------- Slot calculation Evening----------------------------------#####
    
        # Extracting time in string
        eveningfromhrs, eveningfrommin = eveningfromtime.split(':')
        eveningtohrs, eveningtomin = eveningtotime.split(':')

        # Converting time to int
        # fromhrs = int(fromhrs)
        # frommin = int(frommin)
        # tohrs = int(tohrs)
        # tomin = int(tomin)

        # Storing avg time in int format
        avgtime = int(avgtime)
        
        totalmins= (abs(int(eveningfromhrs)- int(eveningtohrs))*60 )+ abs(int(eveningfrommin)-int(eveningtomin))
        Totalslots = totalmins//avgtime

        eveningslot=[str(eveningfromhrs)+':'+str(eveningfrommin)]

        for i in range(1,Totalslots+1):
            eveningfromhrs, eveningfrommin=eveningslot[i-1].split(':')
            if int(eveningfrommin)+avgtime < 60:

                addedmins = int(eveningfrommin)+avgtime
                createdSlot =(eveningfromhrs +':'+str(addedmins))
                eveningslot.append(createdSlot)
            
            elif int(eveningfrommin)+avgtime ==  60:
                addedhrs = (int(eveningfromhrs)+1)
                addedhrs = str(addedhrs)
                if len(addedhrs)==1:
                    addedhrs = '0'+addedhrs
                createdSlot = addedhrs+':'+'00'
                eveningslot.append(createdSlot)


            else:
                remaining_mins = abs(60 - (int(eveningfrommin)+avgtime))
                addedhrs = (int(eveningfromhrs)+1)
                addedhrs = str(addedhrs)
                if len(addedhrs)==1:
                    addedhrs = '0'+addedhrs
                createdSlot = addedhrs+':'+ str(remaining_mins)
                eveningslot.append(createdSlot)

        print(eveningslot)

        eveningSLOT = {}
        slot_countList = []
        start = 0
        hour = (eveningslot[0][0:2])    
        hour = int(hour)
        total_hrs = 0
        for j in range(len(eveningslot)):
            if int(eveningslot[j][0:2]) == hour + 1:       
                slotcount = abs(start - (j))
                start= j
                
                if len(eveningslot[j][0:2]) == 1:
                    time = ("0"+str(hour)+":00") +" -> "+ ("0"+str(hour+1)+":00")
                    eveningSLOT[time]=slotcount

                else:
                    time = (str(hour)+":00") +" -> "+ (str(hour+1)+":00")
                    eveningSLOT[time]=slotcount


                hour = hour +1
                total_hrs = total_hrs+1
        
        print(eveningSLOT)

        slot_instance = slot_table(eveningslotDict=eveningSLOT,morningslotDict=SLOT, doc_username = request.user.username)
        slot_instance.save()

        # datewise_slot_instance = datewise_slot(doc_username= request.user.username ,slotDict=SLOT)
        # datewise_slot_instance.save()



        #-----------------------------------------Slot calculation ends ------------------------------------------
    

        return redirect("doctorhome")



   
    params={
        'username': particular_doc.dusername,
        'fname': particular_doc.fname,
        'lname': particular_doc.lname,
        'email': particular_doc.email,
        'contact': particular_doc.contact,
        'image': particular_doc.image,
        'specialization': particular_doc.specialization,
        'specdegree': particular_doc.specdegree,
        'license': particular_doc.license,
        'desc': particular_doc.desc,
        'morningfromtime' : particular_doc.fromtime,
        'morningtotime' : particular_doc.totime,
        'eveningfromtime' : particular_doc.eveningfromtime,
        'eveningtotime' : particular_doc.eveningtotime,
        'avgtime': particular_doc.avgtime,
        'housenum': particular_doc.housenum,
        'hcity': particular_doc.hcity,
        'hlandmark': particular_doc.hlandmark,
        'hzip': particular_doc.hzip,
        'hstate': particular_doc.hstate,
        'clocation': particular_doc.clocation,
        'ccity': particular_doc.ccity,
        # 'clandmark': particular_doc.clandmark,
        'czip': particular_doc.czip,
        'cstate': particular_doc.cstate,
        


    }


    return render(request, 'doctor/DoctorDetailForm.html', params)
    # return redirect('user/')


def doctorapproved(request):
    doc_bookings = booking.objects.filter(doctor = request.user.username, status = "Approved")

    params={
        "doc_bookings" : doc_bookings
    }

    return render(request, "doctor/Approved.html",params)