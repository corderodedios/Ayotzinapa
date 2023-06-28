from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Page(models.Model):
    PAGES = [
    ('home', 'Gewaltsames Verschwinden'),
    ('school', 'Lehramtschulen'),
    ('ayotzinapa', 'Ayotzinapa'),
    ('students', 'Studenten'),
    ('source', 'Quellen'),
    ('contact', 'Kontakt'),
    ('impressum', 'Impressum'),
    ('legal', 'Data protection'),
]
    title = models.CharField(max_length=20, choices=PAGES, default='home')
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to= 'uploads/')
    image_alt = models.CharField(max_length=50, blank=True)
    source = models.TextField(blank=True)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>') 
    
    def __str__(self):
        return self.get_title_display()

    class Meta:
        verbose_name = 'Seite'
        verbose_name_plural = 'Seiten'

class Time_Step(models.Model):
    YEARS = [
    ('september', '26. September 2014'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
]
    year = models.CharField(choices=YEARS, max_length=10, default='2014')
    date_time = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.date_time

    class Meta:
        verbose_name = 'Zeitpunkt'
        verbose_name_plural = 'Zeitpunkte'

class Victim(models.Model):
    prename = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)
    identified = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'uploads/', blank=True, null= True)
    text = models.TextField(default="")
    birth_year = models.IntegerField(default=2000)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>') 

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = 'Opfer'
        verbose_name_plural = 'Opfer'

class Source(models.Model):
    title = models.CharField(max_length=150)    
    text = models.TextField()

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = 'Quelle'
        verbose_name_plural = 'Quellen' 

class moreInformation(models.Model):
    title = models.CharField(max_length=100)  
    link = models.URLField()  

    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name = 'Mehr Informationen'
        verbose_name_plural = 'Mehr Informationen'