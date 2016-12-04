from PyQt4 import QtGui

import gui.tools as tools

def setupTrait(self):
    # Trait
    self.tab2 = QtGui.QWidget()
    self.tab2.setObjectName(tools._fromUtf8("tab2"))
    self.horizontalLayout_40 = QtGui.QHBoxLayout(self.tab2)
    self.horizontalLayout_40.setObjectName(tools._fromUtf8("horizontalLayout_40"))
    self.tab2_tree = QtGui.QTreeWidget(self.tab2)
    self.tab2_tree.setObjectName(tools._fromUtf8("tab2_tree"))
    self.tab2_tree.headerItem().setText(0, "Name")
    self.tab2_tree.headerItem().setText(1, "Max uses")
    self.horizontalLayout_40.addWidget(self.tab2_tree)
    self.tab2_description = QtGui.QTextBrowser(self.tab2)
    self.tab2_description.setObjectName(tools._fromUtf8("tab2_description"))
    self.horizontalLayout_40.addWidget(self.tab2_description)
    self.main_tab.addTab(self.tab2, "Trait")
    updateTrait(self)
    self.tab2_tree.currentItemChanged.connect(self.updateTraitDescription)

def updateTrait(self):
        race = self.character.race.race_name
        subrace = self.character.race.subrace_name
        trait = self.race_parser.getTrait(race, subrace)
        self.tab2_tree.clear()

        for i in trait:
            max_use = self.trait_parser.getMaxUse(i.get('name'))
            if max_use is None:
                max_use = ''
            item = QtGui.QTreeWidgetItem(self.tab2_tree,
                                         [i.get('name'), max_use])
