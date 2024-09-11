from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/network-status/', consumers.NetworkStatusConsumer.as_asgi()),
]
