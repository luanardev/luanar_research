from django.contrib import admin
from .models import Innovation

# Register your models here.
class InnovationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'patent', 'year_of_innovation']
    list_display_links = ['title',]
    search_fields = ['title',]

admin.site.register(Innovation, InnovationAdmin)