from django.urls import path

from .views import home, create_post, like_post, comment_on_post, like_comment


app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('create_post/',create_post, name='create_post'),
    path('like_post/',like_post, name='like_post'),
    path('comment_on_post/',comment_on_post, name='comment_on_post'),
    path('like_comment/',like_comment, name='like_comment'),
]
