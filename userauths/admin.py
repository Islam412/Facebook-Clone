from django.contrib import admin
from userauths.models import User , Profile 


class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email', 'gender']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'verified']


admin.site.register(User, UserCustomAdmin)
admin.site.register(Profile, ProfileAdmin)