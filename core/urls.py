from django.urls import path

from .views import home, create_post, like_post, comment_on_post, like_comment, reply_comment, delete_comment, delete_reply_comment, post_detail, add_friend, accept_friend_request

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('post/<slug:slug>/',post_detail, name='post_detail'),
    
    # Ajax urls
    path('create_post/',create_post, name='create_post'),
    path('like_post/',like_post, name='like_post'),
    path('comment_on_post/',comment_on_post, name='comment_on_post'),
    path('like_comment/',like_comment, name='like_comment'),
    path('reply_comment/',reply_comment, name='reply_comment'),
    path('delete_comment/',delete_comment, name='delete_comment'),
    path('delete_reply_comment/',delete_reply_comment, name='delete_reply_comment'),
    path('add_friend/',add_friend , name='add_friend'),
    path('accept_friend_request/',accept_friend_request , name='accept_friend_request'),
]
