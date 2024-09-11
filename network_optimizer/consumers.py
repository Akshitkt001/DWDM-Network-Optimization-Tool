import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NetworkStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process the received data and send back a response
        await self.send(text_data=json.dumps({
            'message': 'Data received'
        }))
