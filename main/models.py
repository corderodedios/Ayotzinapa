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
    image = models.ImageField(upload_to = 'uploads/', blank=True, null= True)
    text = models.TextField(default="")
    birth_year = models.IntegerField(default=2000)
    birth_city = models.CharField(max_length=150, default="")
    audio = models.FileField(upload_to='audio', null=True, blank=True)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>') 

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = 'Opfer'
        verbose_name_plural = 'Opfer'

class Source_Category(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Quellenkategorie'
        verbose_name_plural = 'Quellenkategorien'

class Source(models.Model):
    category = models.ForeignKey(Source_Category, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=150)    
    text = models.TextField()

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = 'Quelle'
        verbose_name_plural = 'Quellen'

class Process_Documentation_Section(models.Model):
    title = models.CharField(max_length=150) 
    text = models.TextField()

    class Meta:
        verbose_name = 'Dokumentations Abschnitt'
        verbose_name_plural = 'Dokumentations Abschnitte'    
   
class Process_Documentation_Image(models.Model):
    image = models.ImageField(upload_to = 'uploads/')
    image_alt = models.CharField(max_length=50, blank=True)
    process_documentation_section = models.ForeignKey(Process_Documentation_Section, on_delete=models.CASCADE, null=True, blank=True) 
    big = models.BooleanField(default=False)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')       
    
    class Meta:
        verbose_name = 'Prozess Abschnitt Bild'
        verbose_name_plural = 'Prozess Abschnitt Bilder'