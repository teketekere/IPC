import socket
from socketServer import SocketServer


if __name__ == '__main__':
    host = socket.gethostbyname('localhost')
    port = 19001
    ss = SocketServer(host, port)
    ss.open()
    while True:
        data = ss.read()
        if data is None:
            raise ValueError("Read value is null. Shutdown server.")
            break
        print(data)
        if(data == 'end'):
            print('Received endcode. Shutdown server.')
            break
    ss.close()
