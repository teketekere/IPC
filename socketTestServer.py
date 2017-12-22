from RealtimePlot import RealtimePlot
import socket
from socketServer import SocketServer


def getReceivedValue(server):
    return server.read()


def printReceivedValue(server):
    rtP = RealtimePlot(interval=0.25, x_range=5)
    rtP.initializeFig()
    while True:
        data = getReceivedValue(ss)
        if(validateData(data)):
            data = str(data).split(",")
            print(data)
            rtP.updateFig(data)
        else:
            break


def validateData(data):
    ret = True
    if data is None:
        raise ValueError("Read value is null. Shutdown server.")
        ret = False
    if(data == 'end'):
        print('Received endcode. Shutdown server.')
        ret = False
    return ret


if __name__ == '__main__':
    print('Start server')
    # host = socket.gethostbyname('localhost')
    host = "192.168.1.1"
    port = 19001
    ss = SocketServer(host, port)
    ss.open()
    printReceivedValue(ss)
    ss.close()
