from PyQt4 import QtGui, QtCore
from core.network.server import TCPServer

import gui.tools as tools
from gui.player.character_play import CharacterPlay
from gui.dm.setup_main import setupDMMain

class DungeonMasterGui():
    template_css = """QProgressBar::chunk
    {
    background-color: %s;
    }"""
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(tools._fromUtf8("MainWindow"))
        MainWindow.resize(1005, 719)
        MainWindow.setWindowTitle("Dungeon Master")
        self.main_window = MainWindow

        self.server = TCPServer(self)
        # Create main tab
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(
            tools._fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        setupDMMain(self)

    def openCharacter(self, value):
        character = None
        for socket, temp_char in self.server.list_socket:
            if value.text(0) == temp_char.name:
                character = temp_char
        self.char_play = CharacterPlay()
        self.char_play.setupUi(character, dm=True)
        self.char_play.show()


    def updateList(self):
        self.tree_widget.clear()
        message = "You have " + str(len(self.server.list_socket))
        message = message + " player"
        if len(self.server.list_socket) > 1:
            message = message + 's'
        self.statusbar.showMessage(message)
        for connection, character in self.server.list_socket:
            value = [character.name, character.player,
                     character.dnd_class.class_name, None, None,
                     None, None]
            for i in range(len(value)):
                if value[i] is None:
                    value[i] = ""
            item = QtGui.QTreeWidgetItem(self.tree_widget, value)
            # damage
            dmg_button = QtGui.QPushButton("Take Damage")
            self.tree_widget.setItemWidget(item, 4, dmg_button)
            dmg_button.clicked.connect(lambda: self.sendDamage(
                connection, character))
            # group
            group_combo = QtGui.QComboBox()
            for i in range(len(self.server.list_socket)):
                group_combo.addItem(str(i))
            self.tree_widget.setItemWidget(item, 6, group_combo)
            # hp
            hp, max_hp = character.getHitPoint()
            progress = QtGui.QProgressBar()
            progress.setMaximum(max_hp)
            progress.setValue(hp)
            progress.setFormat(str(hp) + "/" + str(max_hp))
            progress.setAlignment(QtCore.Qt.AlignCenter)
            color = "green"
            if hp < 0.25*max_hp:
                color = "red"
            elif hp < 0.5*max_hp:
                color = "yellow"
            css = DungeonMasterGui.template_css % color
            progress.setStyleSheet(css)
            self.tree_widget.setItemWidget(item, 3, progress)


    def sendDamage(self, socket, character):
        value, ok = QtGui.QInputDialog.getText(
            self.main_window, 'Input Damage', 'Damage:')
        if ok:
            self.server.sendDataToPlayer(
                socket, "takeDamage", int(value))
