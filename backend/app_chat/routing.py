from django.urls import re_path
from .consumers import WSConsumer, WSChat


ws_urlpatterns = [
    re_path(r'ws/instructions/', WSConsumer.as_asgi()),
    re_path(r'ws/chat/', WSChat.as_asgi()),
]
channel_routing = {
    'websocket.connect': 'chat_server.consumers.WSConsumer.as_asgi()',
    'websocket.receive': 'chat_server.consumers.WSConsumer.as_asgi()',
    'websocket.disconnect': 'chat_server.consumers.WSConsumer.as_asgi()',
}
