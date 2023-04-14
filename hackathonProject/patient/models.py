from django.db import models
from doctor.models import doctordetail

# Create your models here.

#Model for handling patient forms
class patientform(models.Model):

    pusername = models.CharField(max_length=50, default='')
    fname= models.CharField(max_length=50, default='', null= True)
    lname = models.CharField(max_length=50, default='', null= True)
    age = models.IntegerField(null=True)
    height = models.IntegerField( null= True)
    weight = models.IntegerField( null= True)
    bloodgrp= models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=20,null= True)
    pemail = models.EmailField(max_length=50, default='') 
    contact = models.BigIntegerField(null=True)
    state = models.CharField(max_length=50, default='', null= True)
    
    allergy = models.CharField(max_length=20, default='')
    goingonMedications = models.CharField(max_length=20, default='')
    insurance = models.CharField(max_length=20, default='', null= True)
    drughistory = models.CharField(max_length=50, default='', null= True)
    symptoms= models.CharField(max_length=100, default = '', null= True)
    medicalhistory= models.CharField(max_length=100, default = '', null= True)

    def __str__(self):
        
        return self.fname
    

# Model for handling appointment bookings
class booking(models.Model):
    auto_field = models.AutoField(primary_key=True)
    bookingid = models.IntegerField(null=True)
    patientdetail = models.ForeignKey(patientform, on_delete=models.CASCADE, null=True)
    pusername = models.CharField(max_length=50, null = True)
    pfname = models.CharField(max_length=50, null = True)
    doctor = models.CharField(max_length=50, default="", null=True)
    slot = models.CharField(max_length=20, default="", null=True)
    slotNum = models.IntegerField(null =True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20, default="Unapproved", null=True)


class datewise_slot(models.Model):
    doc_username = models.CharField(max_length=50, null = True)
    date = models.DateField(null=True)
    updatedSlotdict = models.JSONField(null=True)