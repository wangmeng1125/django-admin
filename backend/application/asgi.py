"""
ASGI config for application project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/

这是一个ASGI应用程序的配置文件，其中包含了ASGI应用程序的路由配置和中间件堆栈配置。
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"



http_application = get_asgi_application()
from application.routing import websocket_urlpatterns
application = ProtocolTypeRouter({
    "http":http_application,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns #指明路由文件是devops/routing.py
        )
    ),
})