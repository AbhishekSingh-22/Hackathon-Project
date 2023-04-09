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

from .models import doctordetail                    # Importing doctordetail table/model



# Create your views here.
def doctorhome(request):
    doctor_detail=doctordetail()

    if doctordetail.objects.filter(dusername=request.user.username):
        return render(request, 'doctor/DoctorHomePage.html')
    
    else:
       
        
        doctor_detail= doctordetail(dusername = request.user.username, fname = request.user.first_name, lname = request.user.last_name, email = request.user.email)
        # doctor_detail.duser = request.user
        # doctor_detail.dusername = request.user.username
        # doctor_detail.fname = request.user.first_name
        # doctor_detail.lname = request.user.last_name
        # doctor_detail.email = request.user.email
        doctor_detail.save()


        return redirect("doctordetailform")



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
    return render(request, "doctor/Approved.html")