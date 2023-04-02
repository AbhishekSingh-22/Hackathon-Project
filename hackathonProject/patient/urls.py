from django.contrib import admin
from django.urls import path, include
from . import views                                            # Importing views.py 

urlpatterns = [
    path('', views.home, name="home"),   

]     