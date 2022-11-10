from django.shortcuts import render
from . import views

# Create your views here.

def home (request):
    return render (request , 'homepage.html')

def model (request):
    
    return
