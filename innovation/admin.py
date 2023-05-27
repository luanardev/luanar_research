from django.contrib import admin
from .models import Innovation,  Innovator

# Register your models here.

class InnovationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'patent', 'year_of_innovation']
    list_display_links = ['title',]
    search_fields = ['title',]

class InnovationMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'innovation', 'media']
    list_display_links = ['innovation',]
    search_fields = ['innovations',]

class InnovatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'innovation', 'title', 'first_name', 'last_name']
    list_display_links = ['innovation',]
    search_fields = ['innovations',]

admin.site.register(Innovation, InnovationAdmin)
admin.site.register(Innovator, InnovatorAdmin)
