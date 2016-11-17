from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def setupRace(self):
    # create tab
    self.tab2 = QtGui.QWidget()
    self.tab2.setObjectName(_fromUtf8("tab2"))
    
    # create race part
    self.verticalLayout_26 = QtGui.QVBoxLayout(self.tab2)
    self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
    self.tab2_race_subrace_layout = QtGui.QHBoxLayout()
    self.tab2_race_subrace_layout.setContentsMargins(0, -1, -1, -1)
    self.tab2_race_subrace_layout.setObjectName(_fromUtf8("tab2_race_subrace_layout"))
    self.tab2_race_layout = QtGui.QGroupBox("Race", self.tab2)
    self.tab2_race_layout.setObjectName(_fromUtf8("tab2_race_layout"))
    self.verticalLayout = QtGui.QVBoxLayout(self.tab2_race_layout)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.tab2_race_choice_layout = QtGui.QHBoxLayout()
    self.tab2_race_choice_layout.setObjectName(_fromUtf8("tab2_race_choice_layout"))
    self.tab2_race_choice_combo = QtGui.QComboBox(self.tab2_race_layout)
    for i in self.race_parser.getListRace():
        self.tab2_race_choice_combo.addItem(i)
    self.tab2_race_choice_combo.activated[str].connect(self.changeRace)
    self.tab2_race_choice_combo.setMinimumSize(QtCore.QSize(150, 5))
    self.tab2_race_choice_combo.setObjectName(_fromUtf8("tab2_race_choice_combo"))
    self.tab2_race_choice_layout.addWidget(self.tab2_race_choice_combo)
    spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.tab2_race_choice_layout.addItem(spacerItem4)
    self.verticalLayout.addLayout(self.tab2_race_choice_layout)
    self.tab2_race_description = QtGui.QTextBrowser(self.tab2_race_layout)
    self.tab2_race_description.setObjectName(_fromUtf8("tab2_race_description"))
    self.verticalLayout.addWidget(self.tab2_race_description)
    self.tab2_race_subrace_layout.addWidget(self.tab2_race_layout)

    # subrace
    self.tab2_subrace_layout = QtGui.QGroupBox("Subrace", self.tab2)
    self.tab2_subrace_layout.setObjectName(_fromUtf8("tab2_subrace_layout"))
    self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab2_subrace_layout)
    self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
    self.tab2_subrace_choice_layout = QtGui.QHBoxLayout()
    self.tab2_subrace_choice_layout.setObjectName(_fromUtf8("tab2_subrace_choice_layout"))
    self.tab2_subrace_choice_combo = QtGui.QComboBox(self.tab2_subrace_layout)
    self.tab2_subrace_choice_combo.activated[str].connect(self.changeSubrace)
    self.tab2_subrace_choice_combo.setMinimumSize(QtCore.QSize(150, 5))
    self.tab2_subrace_choice_combo.setObjectName(_fromUtf8("tab2_subrace_choice_combo"))
    self.tab2_subrace_choice_combo.addItem("Mountain Dwarf")
    self.tab2_subrace_choice_layout.addWidget(self.tab2_subrace_choice_combo)
    spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.tab2_subrace_choice_layout.addItem(spacerItem5)
    self.verticalLayout_2.addLayout(self.tab2_subrace_choice_layout)
    self.tab2_subrace_description = QtGui.QTextBrowser(self.tab2_subrace_layout)
    self.tab2_subrace_description.setObjectName(_fromUtf8("tab2_subrace_description"))
    self.verticalLayout_2.addWidget(self.tab2_subrace_description)
    self.tab2_race_subrace_layout.addWidget(self.tab2_subrace_layout)
    self.verticalLayout_26.addLayout(self.tab2_race_subrace_layout)

    # choices
    self.tab2_choices_layout = QtGui.QGridLayout()
    self.tab2_choices_layout.setContentsMargins(-1, -1, -1, 0)
    self.tab2_choices_layout.setObjectName(_fromUtf8("tab2_choices_layout"))
    self.tab2_choice_list = []
    self.verticalLayout_26.addLayout(self.tab2_choices_layout)

    self.changeRace(self.tab2_race_choice_combo.currentText())
    self.main_tab.addTab(self.tab2, "Race")


