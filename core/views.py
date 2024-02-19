from django.shortcuts import render
from django.utils.text import slugify
from django.http import JsonResponse
from django.utils.timesince import timesince
from django.views.decorators.csrf import csrf_exempt


import shortuuid
from .models import Post



def home(request):
    posts = Post.objects.filter(active=True, visibility='Everyone')
    context = {
        "posts":posts
    }
    return render(request,'core/home.html', context)


@csrf_exempt
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('post-caption')
        visibility = request.POST.get('visibility')
        # image = request.POST.get('post-thumbnail')
        image = request.FILES.get('post-thumbnail')

        print("Title ============", title)
        print("thumbnail ============", image)
        print("visibility ============", visibility)

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