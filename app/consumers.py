import json
import random

from channels.generic.websocket import WebsocketConsumer
from django.core.serializers import serialize

from app import models

class GenerateConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Client connected")

    def disconnect(self, close_code):
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
                self.send(text_data = json.dumps(numberList))
        if text_data == "reset":
            models.numbers.objects.all().delete()
            resetResponse = {'reset': True}
            self.send(text_data = json.dumps(resetResponse))
