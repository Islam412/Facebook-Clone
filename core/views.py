from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.filter(active=True, visibility='Everyone')
    context = {
        "posts":posts
    }
    return render(request,'core/home.html', context)