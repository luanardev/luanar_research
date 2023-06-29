from django.contrib import admin
from .models import User, UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization','research_interests','qualification','bio']

admin.site.register(User)
admin.site.register(UserProfile, UserProfileAdmin)