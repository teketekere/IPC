import asyncio
import socket
from socketServer import SocketServer


async def getReceivedValue(server):
    return server.read()


async def printReceivedValue(server, loop):
    while True:
        data = await getReceivedValue(ss)
        if(validateData(data)):
            print(data)
        else:
            loop.stop()
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
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(printReceivedValue(ss, loop))
    loop.run_forever()
    ss.close()
