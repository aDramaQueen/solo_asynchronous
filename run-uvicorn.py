__author__ = 'Richard Saeuberlich'

import os

import uvicorn
import django

from solo_asynchronous.constants import set_uvicorn_runner

if __name__ == "__main__":
    set_uvicorn_runner(True)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solo_asynchronous.settings')
    django.setup()

    # @see https://www.uvicorn.org/#running-programmatically
    config = uvicorn.Config('solo_asynchronous.asgi:application', workers=1)
    server = uvicorn.Server(config)
    server.run()
