import socket


class SocketServer(object):
    def __init__(self, host, port):
        # host:localhost
        # port:any
        self.port = port
        self.host = host

        self.buffsize = 1024
        # client
        self.conn = None
        # server instance
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # binding
        self.s.bind((self.host, self.port))
        # acceptable client number
        self.s.listen(1)

    def __del__(self):
        self.close()

    def open(self):
        if self.s is not None:
            # conn:client addr:client address
            print("Wait for client...")
            (self.conn, self.addr) = self.s.accept()

    def read(self):
        data = self.conn.recv(self.buffsize).decode('utf-8') if self.conn is not None else None
        return data

    def close(self):
        if self.conn is not None:
            self.conn.close()
        if self.s is not None:
            self.s.close()
