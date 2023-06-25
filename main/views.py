from django.shortcuts import render, get_object_or_404
from .models import Page, Time_Step, Victim, Source, moreInformation

# Create your views here.

def home (request):
    page = Page.objects.get(title='home')
    return render (request, 'home.html', {'page': page})

def school (request):
    page = Page.objects.get(title='school')
    return render (request, 'school.html', {'page': page})

def ayotzinapa (request):
    page = Page.objects.get(title='ayotzinapa')
    time_steps_september = Time_Step.objects.filter(year = 'september')
    time_steps_2014 = Time_Step.objects.filter(year = '2014')
    time_steps_2015 = Time_Step.objects.filter(year = '2015')
    time_steps_2016 = Time_Step.objects.filter(year = '2016')
    time_steps_2017 = Time_Step.objects.filter(year = '2017')
    time_steps_2018 = Time_Step.objects.filter(year = '2018')
    time_steps_2019 = Time_Step.objects.filter(year = '2019')
    time_steps_2020 = Time_Step.objects.filter(year = '2020')
    time_steps_2021 = Time_Step.objects.filter(year = '2021')
    time_steps_2022 = Time_Step.objects.filter(year = '2022')
    time_steps_2023 = Time_Step.objects.filter(year = '2023')
    
    return render (request, 'ayotzinapa.html', {'page': page, 
                                                'time_steps_september': time_steps_september, 
                                                'time_steps_2014': time_steps_2014, 
                                                'time_steps_2015': time_steps_2015, 
                                                'time_steps_2016': time_steps_2016, 
                                                'time_steps_2017': time_steps_2017, 
                                                'time_steps_2018': time_steps_2018,
                                                'time_steps_2019': time_steps_2019,
                                                'time_steps_2020': time_steps_2020,
                                                'time_steps_2021': time_steps_2021,
                                                'time_steps_2022': time_steps_2022,
                                                'time_steps_2023': time_steps_2023})

def source (request):
    page = Page.objects.get(title='source')
    sources = Source.objects.all()
    moreInfos = moreInformation.objects.all()
    return render (request, 'source.html', {'page': page, 'sources': sources, 'moreInfos': moreInfos})

def contact (request):
    page = Page.objects.get(title='contact')
    return render (request, 'contact.html', {'page': page})

def students (request):
    first_column_students = Victim.objects.all()[:23]
    second_column_students = Victim.objects.all()[24:43]
    return render (request, 'students.html', {'first_column_students': first_column_students, 'second_column_students': second_column_students})

def student (request, id):
    student= get_object_or_404(Victim, pk=id)
    return render (request, 'student.html', {'student': student})

def impressum (request):
    page = Page.objects.get(title='impressum')
    return render (request, 'impressum.html', {'page': page})

def legal (request):
    page = Page.objects.get(title='legal')
    return render (request, 'legal.html', {'page': page})