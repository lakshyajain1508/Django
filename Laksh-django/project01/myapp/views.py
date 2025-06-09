from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import UserProfile

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contactus.html')

def sign_in(request):
    return render(request, 'sign.html')

def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})