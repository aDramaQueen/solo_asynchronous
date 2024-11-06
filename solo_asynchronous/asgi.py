"""
ASGI config for solo_asynchronous project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django

from channels.routing import get_default_application, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from solo_asynchronous.constants import get_uvicorn_runner

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solo_asynchronous.settings')

if get_uvicorn_runner():
    # Guvicorn
    django.setup()
    application = get_default_application()
else:
    # Daphne
    asgi_application = get_asgi_application()
    application = ProtocolTypeRouter({
        'http': asgi_application,
    })
