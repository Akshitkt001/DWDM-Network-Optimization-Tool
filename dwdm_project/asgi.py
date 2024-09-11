import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import network_optimizer.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_optimizer.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            network_optimizer.routing.websocket_urlpatterns
        )
    ),
})
