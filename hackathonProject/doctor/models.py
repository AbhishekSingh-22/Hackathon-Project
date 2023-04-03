from django.db import models
from django.contrib.auth.models import User

# Create your models here
class doctordetail(models.Model):

    #Doctor's general details
    duser = models.ForeignKey(User, on_delete=models.CASCADE)
    dusername = models.CharField(max_length=255)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.BigIntegerField()
    image = models.ImageField(upload_to="doctor/images", default='')
    specialization = models.CharField(max_length=100)
    specdegree = models.FileField(upload_to="doctor/files", default='')
    license = models.FileField(upload_to="doctor/files", default='')

    # When doctor is available
    fromtime = models.CharField(max_length=5)
    totime = models.CharField(max_length=5)

    #avg amount of time required to see a patient
    avgtime= models.CharField(max_length=20)

    # Doctor's Home address details
    housenum= models.CharField(max_length= 75)
    hcity = models.CharField(max_length=20)
    hlandmark = models.CharField(max_length=50)
    hzip = models.IntegerField(default=0)
    hstate = models.CharField(max_length=50)

    #Doctor's clinic/hospital address details
    clocation= models.CharField(max_length= 75)
    ccity = models.CharField(max_length=20)
    clandmark = models.CharField(max_length=50)
    czip = models.IntegerField(default=0)
    cstate = models.CharField(max_length=50)

    # name = 'Dr. '+ fname + ' '+ lname


    def __str__(self):
        
        return self.fname