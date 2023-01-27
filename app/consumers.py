import json
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.serializers import serialize

from app import models


class GenerateConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "defaultroom"
        self.room_group_name = "defaultgroup"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        print("Client connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        print("Client disconnected")

    def receive(self, text_data):
        # Generate and send number here
        print("Received request from client", text_data)
        if text_data == "generate":
            newInstance = models.numbers(number=random.randint(1, 100))
            newInstance.save()
            numbers = models.numbers.objects.all()
            if numbers is not None:
                numberList = []
                for number in numbers:
                    numberList.append(number.number)
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name, {"type": "send_resp", "message": numberList}
                )
                # self.send(text_data = json.dumps(numberList))
        if text_data == "reset":
            models.numbers.objects.all().delete()
            resetResponse = {'reset': True}
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "send_resp", "message": resetResponse}
            )
            # self.send(text_data = json.dumps(resetResponse))

    def send_resp(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(message))

