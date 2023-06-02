from django.shortcuts import render
from .models import Page, Time_Step

# Create your views here.

def home (request):
    page = Page.objects.get(title='home')
    return render (request, 'home.html', {'page': page})

def school (request):
    page = Page.objects.get(title='school')
    return render (request, 'school.html', {'page': page})

def ayotzinapa (request):
    page = Page.objects.get(title='ayotzinapa')
    time_steps = Time_Step.objects.all()
    time_steps = time_steps.order_by('year')
    return render (request, 'ayotzinapa.html', {'page': page, 'time_steps': time_steps})

def documentation (request):
    page = Page.objects.get(title='documentation')
    return render (request, 'documentation.html', {'page': page})

def source (request):
    page = Page.objects.get(title='source')
    return render (request, 'source.html')

def contact (request):
    page = Page.objects.get(title='contact')
    return render (request, 'contact.html', {'page': page})
