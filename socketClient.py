import socket


class SocketClient:
    def __init__(self, host, port):
        # host:localhost
        # port:80
        self.port = port
        self.host = host

        # server instance
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.host, self.port))

    def send(self, message):
        # message:string
        # encodeしてbytesにしないとエラー
        msg = message.encode()
        self.s.send(msg)

    def close(self):
        if self.s is not None:
            self.s.close()
