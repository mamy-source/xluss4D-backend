from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'adresse')

admin.site.register(UserProfile, UserProfileAdmin)
