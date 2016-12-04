import pickle
from PyQt4 import QtNetwork


class TCPServer(QtNetwork.QTcpServer):
    def __init__(self, parent, port=27955):
        self.parent = parent
        super(QtNetwork.QTcpServer, self).__init__(parent.main_window)
        self.newConnection.connect(self.onNewConnection)
        # [Connection, Character]
        self.list_socket = []
        self.listen(port=port)
        print "Server is running on port ", port


    def onNewConnection(self):
        self.list_socket.append([self.nextPendingConnection(), None])
        self.list_socket[-1][0].readyRead.connect(self.readData)
        #self.serverAddress()

    def readData(self):
        for i in self.list_socket:
            temp = str(i[0].readAll())
            if len(temp) > 0:
                str_type, text = temp.split(",", 1)
                i[1] = pickle.loads(text)

        self.parent.updateList()
