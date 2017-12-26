import numpy as np
import os
import pickle
from RealtimePlot import RealtimePlot
# if use socket.gethostbyname()
import socket
from sklearn.ensemble import IsolationForest
from socketServer import SocketServer


def getReceivedValue(server):
    return server.read()


def printReceivedValue(server, clf):
    rtP = RealtimePlot(interval=0.25, x_range=5)
    rtP.initializeFig()
    while True:
        data = getReceivedValue(ss)
        if(validateData(data)):
            data = str(data).split(",")
            if(not all([d == float(0.0) for d in data])):
                data = np.array(data, dtype=float)
                pred = clf.decision_function(data.reshape(-1, 1))
                rtP.updateFig(data, pred)
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


def fitIsolationForest(server, path):
    datal = list()
    thresh = 100 * 120
    while len(datal) < thresh:
        data = getReceivedValue(ss)
        if(validateData(data)):
            data = str(data).split(",")
            if(not all([d == float(0.0) for d in data])):
                datal.extend(data)
            msg = "datal.length = " + str(len(datal))
            print(msg)
        else:
            break
    server.close()
    datal = np.array(datal).reshape(-1, 1)
    clf = IsolationForest()
    clf.fit(datal)
    with open(path, 'wb') as f:
        pickle.dump(clf, f)


if __name__ == '__main__':
    print('Start server')
    # host = socket.gethostbyname('localhost')
    host = "192.168.1.1"
    port = 19001
    ss = SocketServer(host, port)
    ss.open()
    path = "isolationForest.model"
    # already learned?
    if(not os.path.exists(path)):
        print("go to learn mode")
        fitIsolationForest(ss, path)
        ss.close()
    else:
        print("go to demo mode")
        with open(path, 'rb') as f:
            clf = pickle.load(f)
        printReceivedValue(ss, clf)
        ss.close()
