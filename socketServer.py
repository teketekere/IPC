import socket


class SocketServer:
    def __init__(self, host, port):
        # host:localhost
        # port:80
        self.port = port
        self.host = host

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
            # temp
            while True:
                data = self.conn.recv(1024).decode('utf-8')
                print(data)
                if data == 'end':
                    break

    def close(self):
        if self.s is not None:
            self.s.close()
        if self.conn is not None:
            self.conn.close()
