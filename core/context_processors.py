# core/context_processors.py

from core.models import FriendRequest

def my_context_processors(request):
    try:
        friend_request = FriendRequest.objects.filter(receiver=request.user)
    except:
        friend_request = None

    return {
        'friend_request': friend_request
    }
