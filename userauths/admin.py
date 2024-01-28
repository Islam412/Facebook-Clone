from django.contrib import admin
from userauths.models import User , Profile 


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email', 'gender']




admin.site.register(User)
admin.site.register(Profile)