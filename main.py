from PyQt4 import QtCore, QtGui
import sys
import argparse

from gui.player.character_loader import CharacterLoader
from gui.dm.dungeon_master_gui import DungeonMasterGui

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-role",
                        action="store",
                        dest="role",
                        default="player",
                        help="player or dm's role",
                        metavar="STRING")
    opt = parser.parse_args()

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    if opt.role == 'player':
        f = CharacterLoader()
    elif opt.role == 'dm':
        f = DungeonMasterGui()

    f.setupUi(w)
    w.show()
    sys.exit(app.exec_())
