from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def setupClass(self):
    # tab
    self.tab3 = QtGui.QWidget()
    self.tab3.setObjectName(_fromUtf8("tab3"))
    self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab3)
    self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
    self.tab3_layout = QtGui.QGridLayout()
    self.tab3_layout.setObjectName(_fromUtf8("tab3_layout"))
    # description
    self.tab3_class_description = QtGui.QTextBrowser(self.tab3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_class_description.sizePolicy().hasHeightForWidth())
    self.tab3_class_description.setSizePolicy(sizePolicy)
    self.tab3_class_description.setObjectName(_fromUtf8("tab3_class_description"))
    self.tab3_layout.addWidget(self.tab3_class_description, 0, 1, 1, 1)
        
    self.tab3_specialization_description = QtGui.QTextBrowser(self.tab3)
    self.tab3_specialization_description.setObjectName(_fromUtf8("tab3_specialization_description"))
    self.tab3_layout.addWidget(self.tab3_specialization_description, 1, 1, 1, 1)

    # Choice
    sizePolicy = QtGui.QSizePolicy(
        QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    
    self.tab3_class_choice_layout = QtGui.QVBoxLayout()
    
    spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.tab3_class_choice_layout.addItem(spacer)

    self.tab3_class_choice_layout.setObjectName(_fromUtf8("tab3_class_choice_layout"))
    self.tab3_class_label = QtGui.QLabel("Class", self.tab3)
    self.tab3_class_label.setSizePolicy(sizePolicy)
    self.tab3_class_label.setObjectName(_fromUtf8("tab3_class_label"))
    self.tab3_class_choice_layout.addWidget(self.tab3_class_label)
    self.tab3_class_combo = QtGui.QComboBox(self.tab3)
    self.tab3_class_combo.setSizePolicy(sizePolicy)
    for i in self.class_parser.getListClass():
        self.tab3_class_combo.addItem(i)
    self.tab3_class_combo.activated[str].connect(self.changeClass)
    self.tab3_class_combo.setObjectName(_fromUtf8("tab3_class_combo"))
    self.tab3_class_choice_layout.addWidget(self.tab3_class_combo)
    # specialization
    self.tab3_specialization_label = QtGui.QLabel("Specialization", self.tab3)
    self.tab3_specialization_label.setSizePolicy(sizePolicy)
    self.tab3_specialization_label.setObjectName(_fromUtf8("tab3_specialization_label"))
    self.tab3_class_choice_layout.addWidget(self.tab3_specialization_label)
    
    self.tab3_specialization_combo = QtGui.QComboBox(self.tab3)
    self.tab3_specialization_combo.activated[str].connect(self.changeSpecialization)
    self.tab3_specialization_combo.setMinimumSize(QtCore.QSize(120, 0))
    self.tab3_specialization_combo.setSizePolicy(sizePolicy)
    self.tab3_specialization_combo.setObjectName(_fromUtf8("tab3_specialization_combo"))
    self.tab3_class_choice_layout.addWidget(self.tab3_specialization_combo)
    self.tab3_layout.addLayout(self.tab3_class_choice_layout, 0, 0, 1, 1)

    spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.tab3_class_choice_layout.addItem(spacer)

    self.tab3_choices_layout = QtGui.QGridLayout()
    self.tab3_layout.addLayout(self.tab3_choices_layout, 1, 0, 1, 1)
    self.tab3_choice_list = []
    self.tab3_choices_layout.setObjectName(_fromUtf8("tab3_choice_layout"))
    self.horizontalLayout_9.addLayout(self.tab3_layout)

    self.changeClass(self.tab3_class_combo.currentText())
    self.main_tab.addTab(self.tab3, "Class")

