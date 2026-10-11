from django.shortcuts import render
from datetime import datetime
from .models import Skill

def home(request):
    skills = Skill.objects.all()          # Get all skills from database
    context = {
        'name': 'Flutter Developer',
        'framework': 'Django 6.1',
        'current_time': datetime.now(),
        'skills': skills,                  # Now coming from database
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')