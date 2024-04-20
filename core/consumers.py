from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json

from userauths.models import User, Profile
from core.models import ChatMessage


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_rote']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )