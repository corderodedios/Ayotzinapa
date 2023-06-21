from django.contrib import admin
from .models import Page, Time_Step, Victim, Source, moreInformation

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

class Time_StepAdmin(admin.ModelAdmin):
    list_display=['year', '__str__']

class VictimAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']


admin.site.register(Page, PageAdmin)
admin.site.register(Time_Step, Time_StepAdmin)
admin.site.register(Victim, VictimAdmin)
admin.site.register(Source)
admin.site.register(moreInformation)