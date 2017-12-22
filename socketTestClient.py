import numpy as np
import socket
from socketClient import SocketClient
import time


if __name__ == '__main__':
    # host = socket.gethostbyname('localhost')
    host = "192.168.1.1"
    port = 19001
    sc = SocketClient(host, port)
    sc.connect()
    for iter in range(1000):
        msg = str(np.sin(float(iter)))
        sc.send(msg)
        time.sleep(0.25)

    msg = "end"
    sc.send(msg)
    sc.close()
