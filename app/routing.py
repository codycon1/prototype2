from django.template.defaulttags import url
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path(r"generate", consumers.GenerateConsumer.as_asgi()),
]