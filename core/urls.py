from django.urls import path

from .views import home, create_post, like_bost


app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('create_post/',create_post, name='create_post'),
    path('like_bost/',like_bost, name='like_bost'),
]
