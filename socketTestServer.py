from socketServer import SocketServer
import socket

if __name__ == '__main__':
    host = socket.gethostbyname('localhost')
    port = 17001
    ss = SocketServer(host, port)
    ss.open()
    ss.close()
