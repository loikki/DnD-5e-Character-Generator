setupEquipment(self)
setupStat(self)

self.tab1_experienceLabel = QtGui.QLabel("Experience", self.tab1_character_layout)
self.tab1_experienceLabel.setObjectName(_fromUtf8("tab1_experienceLabel"))
self.tab1_character_form.setWidget(10, QtGui.QFormLayout.LabelRole, self.tab1_experienceLabel)
self.tab1_experienceSpinBox = QtGui.QSpinBox(self.tab1_character_layout)
self.tab1_experienceSpinBox.valueChanged.connect(self.character.setExperience)
self.tab1_experienceSpinBox.setMaximum(400000)
self.tab1_experienceSpinBox.setObjectName(_fromUtf8("tab1_experienceSpinBox"))
self.tab1_character_form.setWidget(10, QtGui.QFormLayout.FieldRole, self.tab1_experienceSpinBox)

