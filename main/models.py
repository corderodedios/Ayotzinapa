from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Page(models.Model):
    PAGES = [
    ('home', 'Gewaltsames Verschwinden'),
    ('school', 'Lehramtschulen'),
    ('ayotzinapa', 'Ayotzinapa'),
    ('documentation', 'Prozess Dokumentation'),
    ('source', 'Quellen'),
    ('contact', 'Kontakt'),
    ('impressum', 'Impressum'),
    ('legal', 'Data protection'),
]
    title = models.CharField(max_length=20, choices=PAGES, default='home')
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to= 'uploads/')
    image_alt = models.CharField(max_length=50, blank=True)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>') 
    
    def __str__(self):
        return self.title

class Time_Step(models.Model):
    year = models.IntegerField()
    date_time = models.CharField(max_length=20)
    text = models.TextField()


class Victim(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class Source_Category(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()

    def __str__(self):
        return self.name

class Source(models.Model):
    category = models.ForeignKey(Source_Category, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=150)    
    text = models.TextField()

    def __str__(self):
        return self.title    

class Process_Documentation(models.Model):
    image = models.ImageField(upload_to = 'uploads/')

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')     