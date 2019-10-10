from typing import (Optional, Dict)

from functools import partial

from http.server import HTTPServer
from socket import (socket, SOCK_STREAM, AF_INET)
from threading import Thread

from .router import Router
from .handler import Handler
from .page import Page


class Server:

    RouterConfig = Optional[Dict[str, Page]]

    def __init__(self):

        _socket = socket(AF_INET, type=SOCK_STREAM)
        _socket.bind(('localhost', 0))
        self.sa = _socket.getsockname()
        _socket.close()

    def __str__(self):
        return "http://{0}:{1}".format(*self.sa)

    def defaults(self) -> RouterConfig:
        """ return new instance of default rules """
        return {'.*': Page("ok").exists()}

    def router(self, config: RouterConfig = None):
        self.rules = config or self.defaults()
        handler = partial(Handler, Router(self.rules))
        self._server = HTTPServer(self.sa, handler)
        server_thread = Thread(target=self._server.serve_forever)
        server_thread.setDaemon(True)
        server_thread.start()

        return str(self)

    def destroy(self):
        self._server.shutdown()
