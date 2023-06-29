from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'title','license', 'collection']
    list_display_links = ['author','title','license', 'collection']
    search_fields = ['title', 'license', 'collection']

admin.site.register(Publication, PublicationAdmin)