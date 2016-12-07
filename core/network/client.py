import pickle
from copy import deepcopy
from os.path import join
from os import remove
from PyQt4 import QtNetwork

class TCPClient(QtNetwork.QTcpSocket):
    def __init__(self, parent, ip_address, port=27955):
        super(QtNetwork.QTcpSocket, self).__init__(parent)

        self.parent = parent
        self.ip_address = ip_address
        self.connectToHost(str(self.ip_address), port)
        self.readyRead.connect(self.readDataFromDM)
        self.sendInitDataToDM()

    def readDataFromDM(self):
        text = str(self.readAll())
        text = text.split(",", 1)
        if 'takeDamage' in text[0]:
            self.parent.takeDamage(int(text[1]))
        elif "money" in text[0]:
            self.parent.character.money = int(text[1])
            self.parent.updateMoney()
            
    def sendInitDataToDM(self):
        character = deepcopy(self.parent.character)
        character.image = None
        text = pickle.dumps(character)
        self.writeData('file,' + text)

    def sendDataToDM(self, function, value):
        if "heal" in function:
            self.writeData('heal, ' + str(value))

        if "money" in function:
            self.writeData("money, " + str(value))
