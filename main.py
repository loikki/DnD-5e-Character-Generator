from PyQt4 import QtCore, QtGui
import sys

from gui.player.character_loader import CharacterLoader


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    f = CharacterLoader()
    f.setupUi(w)
    w.show()
    sys.exit(app.exec_())
