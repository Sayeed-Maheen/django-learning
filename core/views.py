from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Skill
from .forms import SkillForm

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
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm()

    return render(request, 'core/skill_create.html', {'form': form})

def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('home')

def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'core/skill_edit.html', {'form': form})