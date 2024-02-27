from django.urls import path

from .views import home, create_post, like_post, Comment_on_post


app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('create_post/',create_post, name='create_post'),
    path('like_post/',like_post, name='like_post'),
    path('Comment_on_post/',Comment_on_post, name='Comment_on_post'),
]
