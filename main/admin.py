from django.contrib import admin
from .models import Page, Time_Step, Victim, Source, Process_Documentation, Source_Category

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

class VictimAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

class Process_documentationAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Page, PageAdmin)
admin.site.register(Time_Step)
admin.site.register(Victim, VictimAdmin)
admin.site.register(Source)
admin.site.register(Source_Category)
admin.site.register(Process_Documentation, Process_documentationAdmin)