from django.shortcuts import render , redirect
from django.http import HttpResponse

def Home(request):
    context = {'variable':'Home page'}
    return render(request, 'home.html', context)

def About(request):
    context = {'variable':'About us page'}
    return render(request, 'about.html',context)

def contact(request):
    return render(request,'contactus.html')

from .models import UserProfile

def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})