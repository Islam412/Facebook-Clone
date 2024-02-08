from django.contrib import admin
from userauths.models import User , Profile 


class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'verified']
    list_editable = ['verified']


admin.site.register(User, UserCustomAdmin)
admin.site.register(Profile, ProfileAdmin)