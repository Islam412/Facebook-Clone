from django.urls import path

from core.views import home


app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
]
