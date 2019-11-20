from functools import partial

from http.server import HTTPServer

from socket import (socket, SOCK_STREAM, AF_INET)
from typing import (Union, Optional)

from threading import Thread
from pathlib import Path

from deadlinks.serving.handler import Handler
from deadlinks.serving.router import Router


class SimpleServer:

    def __init__(self, web_root: Union[str, Path], web_path: Optional[str]) -> None:

        self.web_path = "/" if not web_path else web_path
        if not self.web_path.startswith("/"):
            self.web_path = "/" + self.web_path

        if not isinstance(web_root, Path):
            web_root = Path(web_root)

        _router = Router(web_root.resolve(), self.web_path)

        _socket = socket(AF_INET, type=SOCK_STREAM)
        _socket.bind(('localhost', 0))
        self._sa = _socket.getsockname()
        _socket.close()

        # implement correct type annotation, when change
        # https://github.com/python/mypy/issues/1484

        self._server = HTTPServer(self._sa, partial(Handler, _router)) # type: ignore
        server_thread = Thread(target=self._server.serve_forever)
        server_thread.setDaemon(True)
        server_thread.start()

    def __str__(self) -> str:
        """ Instance as browsable URL. """

        return self.url()

    def url(self) -> str:
        """ Return URL of running server (including path). """

        return "http://{}:{}{}".format(self._sa[0], self._sa[1], self.web_path)


if __name__ == "__main__":

    import subprocess
    import requests
    import time

    # web_server = SimpleServer(Path("../gobyexample/public"), None)
    web_server = SimpleServer(Path("../gobyexample/public"), "/go/")

    subprocess.run([
        "open",
        web_server.url(),
    ])

    requests.get(web_server.url())
    time.sleep(.5)
    requests.get(web_server.url() + 'panic')
    requests.get(web_server.url() + 'goroutines')
    time.sleep(.5)
    time.sleep(.5)
    time.sleep(.5)

    time.sleep(10)