import json
import webbrowser
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chat.models import CheckUser
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        user = self.scope.get('user')
        if user:
            check_user, cr = CheckUser.objects.get_or_create(   
                user=user
            )
            check_user.is_online = True
            check_user.save()

        self.accept()
    
    def disconnect(self, code):
        user = self.scope.get('user')
        if user:
            check_user, cr = CheckUser.objects.get_or_create(
                user=user
            )
            check_user.is_online = False
            check_user.save()
        print("dustu", self.scope.get('user'))
