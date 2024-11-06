__author__ = 'Richard Saeuberlich'

import uvicorn

from solo_asynchronous.constants import set_uvicorn_runner

if __name__ == "__main__":
    set_uvicorn_runner(True)
    # @see https://www.uvicorn.org/#running-programmatically
    config = uvicorn.Config('solo_asynchronous.asgi:application', workers=1)
    server = uvicorn.Server(config)
    server.run()
