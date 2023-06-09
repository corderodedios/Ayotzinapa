"""
URL configuration for ayotzinapa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home, school, ayotzinapa, source, contact, students, student, legal, impressum

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('school/', school, name='school'),
    path('ayotzinapa/', ayotzinapa, name='ayotzinapa'),
    path('source/', source, name='source'),
    path('contact/', contact, name='contact'),
    path('students/', students, name='students'),
    path('student/<int:id>', student, name='student'),
    path('impressum/', impressum, name='impressum'),
    path('legal/', legal, name='legal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

