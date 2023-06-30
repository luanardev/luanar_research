from django.contrib import admin
from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','start_date','end_date','meeting_type','venue','description']


admin.site.register(Event, EventAdmin)
