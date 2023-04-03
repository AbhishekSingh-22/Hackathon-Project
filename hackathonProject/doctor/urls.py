from django.contrib import admin
from django.urls import path, include
from . import views                                            # Importing views.py 


# creating routes
urlpatterns = [
    path('', views.doctorhome, name="doctorhome"), 
    path('doctordetailform', views.doctordetailform, name="doctordetailform"), 


]       