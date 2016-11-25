from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def setupClass(self):
    # tab
    self.page2 = QtGui.QWizardPage()
    self.page2.setObjectName(_fromUtf8("page2"))
    self.horizontalLayout_9 = QtGui.QHBoxLayout(self.page2)
    self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
    self.page2_layout = QtGui.QGridLayout()
    self.page2_layout.setObjectName(_fromUtf8("page2_layout"))
    # description
    self.page2_class_description = QtGui.QTextBrowser(self.page2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page2_class_description.sizePolicy().hasHeightForWidth())
    self.page2_class_description.setSizePolicy(sizePolicy)
    self.page2_class_description.setObjectName(_fromUtf8("page2_class_description"))
    self.page2_layout.addWidget(self.page2_class_description, 0, 1, 1, 1)
        
    self.page2_specialization_description = QtGui.QTextBrowser(self.page2)
    self.page2_specialization_description.setObjectName(_fromUtf8("page2_specialization_description"))
    self.page2_layout.addWidget(self.page2_specialization_description, 1, 1, 1, 1)

    # Choice
    sizePolicy = QtGui.QSizePolicy(
        QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    
    self.page2_class_choice_layout = QtGui.QVBoxLayout()
    
    spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.page2_class_choice_layout.addItem(spacer)

    self.page2_class_choice_layout.setObjectName(_fromUtf8("page2_class_choice_layout"))
    self.page2_class_label = QtGui.QLabel("Class", self.page2)
    self.page2_class_label.setSizePolicy(sizePolicy)
    self.page2_class_label.setObjectName(_fromUtf8("page2_class_label"))
    self.page2_class_choice_layout.addWidget(self.page2_class_label)
    self.page2_class_combo = QtGui.QComboBox(self.page2)
    self.page2_class_combo.setSizePolicy(sizePolicy)
    for i in self.class_parser.getListClass():
        self.page2_class_combo.addItem(i)
    self.page2_class_combo.activated[str].connect(self.changeClass)
    self.page2_class_combo.setObjectName(_fromUtf8("page2_class_combo"))
    self.page2_class_choice_layout.addWidget(self.page2_class_combo)
    # specialization
    self.page2_specialization_label = QtGui.QLabel("Specialization", self.page2)
    self.page2_specialization_label.setSizePolicy(sizePolicy)
    self.page2_specialization_label.setObjectName(_fromUtf8("page2_specialization_label"))
    self.page2_class_choice_layout.addWidget(self.page2_specialization_label)
    
    self.page2_specialization_combo = QtGui.QComboBox(self.page2)
    self.page2_specialization_combo.activated[str].connect(self.changeSpecialization)
    self.page2_specialization_combo.setMinimumSize(QtCore.QSize(120, 0))
    self.page2_specialization_combo.setSizePolicy(sizePolicy)
    self.page2_specialization_combo.setObjectName(_fromUtf8("page2_specialization_combo"))
    self.page2_class_choice_layout.addWidget(self.page2_specialization_combo)
    self.page2_layout.addLayout(self.page2_class_choice_layout, 0, 0, 1, 1)

    spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.page2_class_choice_layout.addItem(spacer)

    self.page2_choices_layout = QtGui.QGridLayout()
    self.page2_layout.addLayout(self.page2_choices_layout, 1, 0, 1, 1)
    self.page2_choice_list = []
    self.page2_choices_layout.setObjectName(_fromUtf8("page2_choice_layout"))
    self.horizontalLayout_9.addLayout(self.page2_layout)

    self.changeClass(self.page2_class_combo.currentText())
    self.changeSpecialization(self.page2_specialization_combo.currentText())

    return self.page2

