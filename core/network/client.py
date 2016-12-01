from PyQt4 import QtNetwork

class TCPClient(QtNetwork.QTcpSocket):
    def __init__(self, parent, ip_address, port=27955):
        super(QtNetwork.QTcpSocket, self).__init__(parent)

        self.parent = parent
        self.ip_address = ip_address
        self.connectToHost(str(self.ip_address), port)
        self.readyRead.connect(self.readDataFromDM)

    def readDataFromDM(self):
        text = str(self.readAll())
        print text
        text = text.split(",", 2)
        if 'takeDamage' in text[0]:
            self.parent.takeDamage(int(text[1]))
