from PyQt4 import QtGui
from core.network.server import TCPServer

import gui.tools as tools

class DungeonMasterGui():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(tools._fromUtf8("MainWindow"))
        MainWindow.resize(1005, 719)
        MainWindow.setWindowTitle("Dungeon Master")
        self.main_window = MainWindow

        self.server = TCPServer(self)
        # Create main tab
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(tools._fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

    def updateList(self):
        for connection, character in self.server.list_socket:
            print character.name
