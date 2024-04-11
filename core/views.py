from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.http import JsonResponse
from django.utils.timesince import timesince
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



import shortuuid
from .models import Post, Comment, ReplyComment, Friend, FriendRequest, Notification
from userauths.models import User



# Notifications Keys
noti_new_like = "New Like"
noti_new_follower = "New Follower"
noti_friend_request = "Friend Request"
noti_new_comment = "New Comment"
noti_comment_liked = "Comment Liked"
noti_comment_replied = "Comment Replied"
noti_friend_request_accepted = "Friend Request Accepted"


@login_required
def home(request):
    posts = Post.objects.filter(active=True, visibility='Everyone').order_by("-id")   # .order_by("-id") ----->>show modern post
    context = {
        "posts":posts
    }
    return render(request,'core/home.html', context)


@login_required
def post_detail(request, slug):
    post = Post.objects.get(slug=slug, active=True, visibility='Everyone')   # id = request.GET['id]          post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, 'core/post_detail.html', context)


@login_required
def send_notification(user, sender, post, comment, notification_type):
    notification = Notification.objects.create(
        user=user,
        sender=sender,
        post=post,
        comment=comment,
        notification_type=notification_type,
    )
    return notification


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
                "full_name":post.user.profile.full_name,
                "profile_image":post.user.profile.image.url,
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
        
        if post.user != request.user:
            send_notification(post.user, user, post, None, noti_new_like)

    data = {
        'bool':bool,
        'likes':post.likes.all().count(),
    }

    return JsonResponse({'data':data})



def comment_on_post(request):
    id = request.GET['id']
    comment = request.GET['comment']
    post = Post.objects.get(id=id)
    Comment_count = Comment.objects.filter(post=post).count()
    user = request.user

    new_comment = Comment.objects.create(
        post=post,
        comment=comment,
        user=user,
    )
    
    if new_comment.user != post.user:
        send_notification(post.user, user, post, new_comment, noti_new_comment)

    data = {
        'bool' : True,
        'comment' : new_comment.comment,
        "profile_image":new_comment.user.profile.image.url,
        'date' : timesince(new_comment.date),
        'comment_id' : new_comment.id,
        'post_id' : new_comment.post.id,
        'Comment_count' : Comment_count + int(1),
    }

    return JsonResponse({'data':data})


def like_comment(request):
    id = request.GET['id']
    comment = Comment.objects.get(id=id)   # comment = Comment.object.first()
    user = request.user
    bool= False

    if user in comment.likes.all():
        comment.likes.remove(user)
        bool = False
    else:
        comment.likes.add(user)
        bool = True

    data = {
        'bool':bool,
        'likes' :comment.likes.all().count(),
    }

    return JsonResponse({'data':data})


def reply_comment(request):
    id = request.GET['id']
    reply = request.GET['reply']

    comment = Comment.objects.get(id=id)
    user = request.user

    new_reply = ReplyComment.objects.create(
        comment=comment,
        reply=reply,
        user=user,
    )

    data = {
        'bool': True,
        'reply': new_reply.reply,
        'profile_image': new_reply.user.profile.image.url,
        'date': timesince(new_reply.date),
        'reply_id': new_reply.id,
        'post_id': new_reply.comment.post.id,
    }

    return JsonResponse({'data':data})



def delete_comment(request):
    id = request.GET['id']
    comment = Comment.objects.get(id=id)
    comment.delete()

    data = {
        'bool' : True,
    }

    return JsonResponse({'data':data})


def delete_reply_comment(request):
    id = request.GET['id']
    reply = ReplyComment.objects.get(id=id)
    reply.delete()
    
    data = {
        'bool' : True,
    }
    
    return JsonResponse({'data':data})



def add_friend(request):
    sender = request.user
    receiver_id = request.GET['id']
    bool = False
    
    if sender.id == int(receiver_id):
        return JsonResponse({'error':'You cannot send a friend request to yourself'})
    
    receiver = User.objects.get(id=receiver_id)
    
    try:
        friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver)
        if friend_request:
            friend_request.delete()
        bool=False
        return JsonResponse({'error':'Cancelled', 'bool':bool})

    except FriendRequest.DoesNotExist:
        friend_request = FriendRequest(sender=sender, receiver=receiver)
        friend_request.save()
        bool = True
        return JsonResponse({'success':'Sent', 'bool':bool})


def accept_friend_request(request):
    id = request.GET['id']
    
    receiver = request.user
    sender = User.objects.get(id=id)
    
    friend_request = FriendRequest.objects.filter(receiver=receiver, sender=sender).first()
    
    receiver.profile.friends.add(sender)
    sender.profile.friends.add(receiver)
    
    friend_request.delete()
    
    data = {
        'message' : 'Accepted',
        'bool' : True,
    }
    return JsonResponse({"data":data})


def reject_friend_request(request):
    id = request.GET['id']
    
    receiver = request.user
    sender = User.objects.get(id=id)
    
    friend_reject = FriendRequest.objects.filter(receiver=receiver, sender=sender).first()    
    friend_reject.delete()
    
    data = {
        'message' : 'Rejected',
        'bool' : True,
    }
    return JsonResponse({"data":data})


def unfriend(request):
    sender = request.user
    friend_id = request.GET['id']
    bool = False
    
    if sender.id == int(friend_id):
        return JsonResponse({"error":"You cannot unfriend yourself, wait a minute how did you even send yourself a friend request?"})
    
    my_friend = User.objects.get(id=friend_id)
    
    if my_friend in sender.profile.friends.all():
        sender.profile.friends.remove(my_friend)
        my_friend.profile.friends.remove(sender)
        bool = True
        return JsonResponse({"success":"Unfriend Successfully", "bool":bool})
    
    