import json

from channels.generic.websocket import WebsocketConsumer


class GenerateConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Generate and send number here
        self.send(text_date=json.dumps({"number": 0}))
