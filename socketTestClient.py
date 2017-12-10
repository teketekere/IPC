from socketClient import SocketClient
import socket
import time

if __name__ == '__main__':
    host = socket.gethostbyname('localhost')
    port = 17001
    sc = SocketClient(host, port)
    sc.connect()
    for iter in range(5):
        msg = str(iter) + "," + str(iter**2)
        sc.send(msg)
        time.sleep(1)

    msg = "end"
    sc.send(msg)
    sc.close()
