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
        self.list_socket[-1][0].readyRead.connect(lambda: self.readDataFromPlayer(self.list_socket[-1]))
        #self.serverAddress()

    def readDataFromPlayer(self, item_socket):
        socket = item_socket[0]
        character = item_socket[1]
        temp = str(socket.readAll())
        if len(temp) <= 0:
            return
        str_type, text = temp.split(",", 1)
        if character is None or 'file' in str_type:
            character = pickle.loads(text)
        elif "heal" in str_type:
            character.dnd_class.hit_point += int(text)
        elif "money" in str_type:
            character.money = int(text)
        item_socket[1] = character
        self.parent.updateList()

    def sendDataToPlayer(self, socket, function, value):
        character = None
        j = 0
        for i in self.list_socket:
            if i[0] == socket:
                break
            j += 1
        if "takeDamage" in function:
            self.list_socket[j][1].dnd_class.hit_point -= value
            self.list_socket[j][0].write("takeDamage, " + str(value))
        elif "money" in function:
            self.list_socket[j][1].money = value
            self.list_socket[j][0].write("money, " + str(value))

        self.parent.updateList()
