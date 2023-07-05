from django.contrib import admin
from .models import User, Profile
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization','research_interests','qualification']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)