import socket
from socketClient import SocketClient
import time
import psutil


if __name__ == '__main__':
    host = socket.gethostbyname('localhost')
    port = 19001
    sc = SocketClient(host, port)
    sc.connect()
    for _ in range(1000):
        msg = str(psutil.cpu_percent())
        sc.send(msg)
        time.sleep(1)

    msg = "end"
    sc.send(msg)
    sc.close()
