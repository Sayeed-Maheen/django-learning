from django.shortcuts import render, redirect
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

def skill_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        level = request.POST.get('level')

        Skill.objects.create(name=name, level=level)
        return redirect('home')

    return render(request, 'core/skill_create.html')