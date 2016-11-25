from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def setupRace(self):
    # create tab
    self.page1 = QtGui.QWizardPage()
    self.page1.setObjectName(_fromUtf8("page1"))
    
    # create race part
    self.verticalLayout_26 = QtGui.QVBoxLayout(self.page1)
    self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
    self.page1_race_subrace_layout = QtGui.QHBoxLayout()
    self.page1_race_subrace_layout.setContentsMargins(0, -1, -1, -1)
    self.page1_race_subrace_layout.setObjectName(_fromUtf8("page1_race_subrace_layout"))
    self.page1_race_layout = QtGui.QGroupBox("Race", self.page1)
    self.page1_race_layout.setObjectName(_fromUtf8("page1_race_layout"))
    self.verticalLayout = QtGui.QVBoxLayout(self.page1_race_layout)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.page1_race_choice_layout = QtGui.QHBoxLayout()
    self.page1_race_choice_layout.setObjectName(_fromUtf8("page1_race_choice_layout"))
    self.page1_race_choice_combo = QtGui.QComboBox(self.page1_race_layout)
    for i in self.race_parser.getListRace():
        self.page1_race_choice_combo.addItem(i)
    self.page1_race_choice_combo.activated[str].connect(self.changeRace)
    self.page1_race_choice_combo.setMinimumSize(QtCore.QSize(150, 5))
    self.page1_race_choice_combo.setObjectName(_fromUtf8("page1_race_choice_combo"))
    self.page1_race_choice_layout.addWidget(self.page1_race_choice_combo)
    spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.page1_race_choice_layout.addItem(spacerItem4)
    self.verticalLayout.addLayout(self.page1_race_choice_layout)
    self.page1_race_description = QtGui.QTextBrowser(self.page1_race_layout)
    self.page1_race_description.setObjectName(_fromUtf8("page1_race_description"))
    self.verticalLayout.addWidget(self.page1_race_description)
    self.page1_race_subrace_layout.addWidget(self.page1_race_layout)

    # subrace
    self.page1_subrace_layout = QtGui.QGroupBox("Subrace", self.page1)
    self.page1_subrace_layout.setObjectName(_fromUtf8("page1_subrace_layout"))
    self.verticalLayout_2 = QtGui.QVBoxLayout(self.page1_subrace_layout)
    self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
    self.page1_subrace_choice_layout = QtGui.QHBoxLayout()
    self.page1_subrace_choice_layout.setObjectName(_fromUtf8("page1_subrace_choice_layout"))
    self.page1_subrace_choice_combo = QtGui.QComboBox(self.page1_subrace_layout)
    self.page1_subrace_choice_combo.activated[str].connect(self.changeSubrace)
    self.page1_subrace_choice_combo.setMinimumSize(QtCore.QSize(150, 5))
    self.page1_subrace_choice_combo.setObjectName(_fromUtf8("page1_subrace_choice_combo"))
    self.page1_subrace_choice_combo.addItem("Mountain Dwarf")
    self.page1_subrace_choice_layout.addWidget(self.page1_subrace_choice_combo)
    spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.page1_subrace_choice_layout.addItem(spacerItem5)
    self.verticalLayout_2.addLayout(self.page1_subrace_choice_layout)
    self.page1_subrace_description = QtGui.QTextBrowser(self.page1_subrace_layout)
    self.page1_subrace_description.setObjectName(_fromUtf8("page1_subrace_description"))
    self.verticalLayout_2.addWidget(self.page1_subrace_description)
    self.page1_race_subrace_layout.addWidget(self.page1_subrace_layout)
    self.verticalLayout_26.addLayout(self.page1_race_subrace_layout)

    # choices
    self.page1_choices_layout = QtGui.QGridLayout()
    self.page1_choices_layout.setContentsMargins(-1, -1, -1, 0)
    self.page1_choices_layout.setObjectName(_fromUtf8("page1_choices_layout"))
    self.page1_choice_list = []
    self.verticalLayout_26.addLayout(self.page1_choices_layout)

    self.changeRace(self.page1_race_choice_combo.currentText())
    return self.page1


