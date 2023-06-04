from django.contrib import admin
from .models import Page, Time_Step, Victim, Source, Process_Documentation_Section, Process_Documentation_Image, Source_Category

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

class Time_StepAdmin(admin.ModelAdmin):
    list_display=['year', '__str__']

class VictimAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

class Process_Documentation_ImageAdmin(admin.StackedInline):     
    readonly_fields = ['img_preview']
    model = Process_Documentation_Image

@admin.register(Process_Documentation_Section)
class Process_Documentation_SectionAdmin(admin.ModelAdmin):
    inlines = [Process_Documentation_ImageAdmin]

    class Meta:
        model = Process_Documentation_Section

@admin.register(Process_Documentation_Image)
class Process_Documentation_ImageAdmin(admin.ModelAdmin):
    pass   

admin.site.register(Page, PageAdmin)
admin.site.register(Time_Step, Time_StepAdmin)
admin.site.register(Victim, VictimAdmin)
admin.site.register(Source)
admin.site.register(Source_Category)