from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json

from userauths.models import User, Profile
from core.models import ChatMessage


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        sender_username = data.get("sender")
        
        try:
            sender = User.objects.get(username=sender_username)
            profile =  Profile.objects.get(user=sender)
            profile_image = profile.image.url
        except User.DoesNotExist:
            profile_image = ''
            
        receiver = User.objects.get(username=data['receiver'])
        chat_message = ChatMessage(
            sender=sender,
            receiver=receiver,
            message=message,
        )
        chat_message.save()
        
        async_to_sync(self.channel_layer.group_send)(
            {
                'type':"chat_message",
                'message':message,
                'sender':sender,
                'profile_image':profile_image,
                'receiver':receiver,
            }
        )
    
    def chat_message(self,event):
        self.send(text_data=json.dumps(event))