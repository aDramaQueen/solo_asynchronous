"""
ASGI config for solo_asynchronous project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

asgi_application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': asgi_application,
})
