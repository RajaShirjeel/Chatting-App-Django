import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f'chat_{self.user_pk}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Debugging: Print received message on server-side
        print(f"Received message: {message}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        

    async def chat_message(self, event):
        message = event['message']
        
        # Debugging: Print message before sending to WebSocket
        print(f"Sending message: {message}")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
