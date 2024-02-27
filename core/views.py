from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.http import JsonResponse
from django.utils.timesince import timesince
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



import shortuuid
from .models import Post, Comment



@login_required
def home(request):
    posts = Post.objects.filter(active=True, visibility='Everyone').order_by("-id")   # .order_by("-id") ----->>show modern post
    context = {
        "posts":posts
    }
    return render(request,'core/home.html', context)


@csrf_exempt
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('post-caption')
        visibility = request.POST.get('visibility')
        image = request.FILES.get('post-thumbnail')
        

        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:4]


        if title and image:
            post = Post(
                title=title,
                image=image,
                visibility=visibility,
                user=request.user,
                slug=slugify(title) + '-' + str(uniqueid.lower()),
            )
            post.save()

            return JsonResponse({'post' :{
                'title':post.title,
                "image":post.image.url,
                "full_name":post.user.profile.image.url,
                'date':timesince(post.date),
                'id':post.id,
            }})
        else:
            return JsonResponse({'error': 'Image or titile dose not exists'})
        
    return JsonResponse({'data':'sent'})



def like_post(request):
    id = request.GET['id']
    post = Post.objects.get(id=id)
    user = request.user
    bool = False

    if user in post.likes.all():
        post.likes.remove(user)
        bool = False
    else:
        post.likes.add(user)
        bool = True

    data = {
        'bool':bool,
        'likes':post.likes.all().count(),
    }

    return JsonResponse({'data':data})



def Comment_on_post(request):
    id = request.GET['id']
    Comment = request.GET['Comment']
    post = Post.objects.get(id=id)
    Comment_count = Comment.objects.filter(post=post).count()
    user = request.user

    new_comment = Comment.objects.create(
        post=post,
        comment=comment,
        user=user,
    )

    data = {
        'bool' : True,
        'comment' : new_comment.comment,
        'profile_imaage' : new_comment.profile.image.url,
        'date' : timesince(new_comment.date),
        'comment_id' : new_comment.id,
        'post_id' : new_comment.post.id,
        'Comment_count' : Comment_count + int(1),
    }

    return JsonResponse({'data':data})
