from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


def setupCharacterChoice(self):
    # create tab
    self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

    # create character choice tree
    self.character_choice_layout = QtGui.QVBoxLayout()
    self.character_choice_layout.setObjectName(_fromUtf8("character_choice_layout"))
    self.character_choice = QtGui.QListWidget(self.centralwidget)
    self.character_choice.currentRowChanged.connect(self.printSummary)
    self.character_choice.setSortingEnabled(False)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.character_choice.sizePolicy().hasHeightForWidth())
    self.character_choice.setSizePolicy(sizePolicy)
    self.character_choice.setObjectName(_fromUtf8("character_choice"))

    # add the list
    self.character_choice_layout.addWidget(self.character_choice)

    # create buttons
    self.button_layout = QtGui.QHBoxLayout()
    self.button_layout.setObjectName(_fromUtf8("button_layout"))
    self.new_character = QtGui.QPushButton("New Character", self.centralwidget)
    self.new_character.clicked.connect(self.newCharacter)
    self.new_character.setObjectName(_fromUtf8("new_character"))
    self.button_layout.addWidget(self.new_character)
    self.choose_current = QtGui.QPushButton("Load Character", self.centralwidget)
    self.choose_current.setObjectName(_fromUtf8("choose_current"))
    self.choose_current.clicked.connect(self.loadCharacter)
    self.button_layout.addWidget(self.choose_current)
    self.delete_character = QtGui.QPushButton("Delete Character", self.centralwidget)
    self.delete_character.setObjectName(_fromUtf8("delete_character"))
    self.delete_character.clicked.connect(self.deleteCharacter)
    self.button_layout.addWidget(self.delete_character)

    self.character_choice_layout.addLayout(self.button_layout)

    # create summary part
    self.horizontalLayout_2.addLayout(self.character_choice_layout)
    self.summary_layout = QtGui.QGroupBox("Summary", self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.summary_layout.sizePolicy().hasHeightForWidth())
    self.summary_layout.setSizePolicy(sizePolicy)
    self.summary_layout.setObjectName(_fromUtf8("summary_layout"))

    # create class/background/race part + image
    self.verticalLayout_17 = QtGui.QVBoxLayout(self.summary_layout)
    self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
    self.img_background_layout = QtGui.QHBoxLayout()
    self.img_background_layout.setContentsMargins(-1, 0, -1, -1)
    self.img_background_layout.setObjectName(_fromUtf8("img_background_layout"))

    # create class/background/race part
    self.background_layout = QtGui.QFormLayout()
    self.background_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
    self.background_layout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.background_layout.setObjectName(_fromUtf8("background_layout"))
    self.classLabel_2 = QtGui.QLabel("Class", self.summary_layout)
    self.classLabel_2.setObjectName(_fromUtf8("classLabel_2"))
    self.background_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.classLabel_2)
    self.classLineEdit = QtGui.QLineEdit(self.summary_layout)
    self.classLineEdit.setReadOnly(True)
    self.classLineEdit.setObjectName(_fromUtf8("classLineEdit"))
    self.background_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.classLineEdit)
    self.raceLineEdit = QtGui.QLineEdit(self.summary_layout)
    self.raceLineEdit.setReadOnly(True)
    self.raceLineEdit.setObjectName(_fromUtf8("raceLineEdit"))
    self.background_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.raceLineEdit)
    self.specializationLabel_2 = QtGui.QLabel("Specialization", self.summary_layout)
    self.specializationLabel_2.setObjectName(_fromUtf8("specializationLabel_2"))
    self.background_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.specializationLabel_2)
    self.specializationLineEdit = QtGui.QLineEdit(self.summary_layout)
    self.specializationLineEdit.setReadOnly(True)
    self.specializationLineEdit.setObjectName(_fromUtf8("specializationLineEdit"))
    self.background_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.specializationLineEdit)
    self.raceLabel = QtGui.QLabel("Race", self.summary_layout)
    self.raceLabel.setObjectName(_fromUtf8("raceLabel"))
    self.background_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.raceLabel)
    self.backgroundLabel = QtGui.QLabel("Background", self.summary_layout)
    self.backgroundLabel.setObjectName(_fromUtf8("backgroundLabel"))
    self.background_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.backgroundLabel)
    self.backgroundLineEdit = QtGui.QLineEdit(self.summary_layout)
    self.backgroundLineEdit.setReadOnly(True)
    self.backgroundLineEdit.setObjectName(_fromUtf8("backgroundLineEdit"))
    self.background_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.backgroundLineEdit)
    self.experienceLevelLabel = QtGui.QLabel("Experience (Level)", self.summary_layout)
    self.experienceLevelLabel.setObjectName(_fromUtf8("experienceLevelLabel"))
    self.background_layout.setWidget(4, QtGui.QFormLayout.LabelRole, self.experienceLevelLabel)
    self.experienceLevelLineEdit = QtGui.QLineEdit(self.summary_layout)
    self.experienceLevelLineEdit.setReadOnly(True)
    self.experienceLevelLineEdit.setObjectName(_fromUtf8("experienceLevelLineEdit"))
    self.background_layout.setWidget(4, QtGui.QFormLayout.FieldRole, self.experienceLevelLineEdit)
    self.img_background_layout.addLayout(self.background_layout)
    
    # create image
    self.img = QtGui.QLabel(self.summary_layout)
    self.img.setObjectName(_fromUtf8("img"))
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(150)
    self.img.setSizePolicy(sizePolicy)
    self.img_background_layout.addWidget(self.img)

    # create ability layout
    self.verticalLayout_17.addLayout(self.img_background_layout)
    self.ability_layout = QtGui.QGridLayout()
    self.ability_layout.setObjectName(_fromUtf8("ability_layout"))
    self.dex_label = QtGui.QLabel("Dexterity", self.summary_layout)
    self.dex_label.setAlignment(QtCore.Qt.AlignCenter)
    self.dex_label.setObjectName(_fromUtf8("dex_label"))
    self.ability_layout.addWidget(self.dex_label, 0, 1, 1, 1)
    self.con_label = QtGui.QLabel("Constitution", self.summary_layout)
    self.con_label.setAlignment(QtCore.Qt.AlignCenter)
    self.con_label.setObjectName(_fromUtf8("con_label"))
    self.ability_layout.addWidget(self.con_label, 0, 2, 1, 1)
    self.int_label = QtGui.QLabel("Intelligence", self.summary_layout)
    self.int_label.setAlignment(QtCore.Qt.AlignCenter)
    self.int_label.setObjectName(_fromUtf8("int_label"))
    self.ability_layout.addWidget(self.int_label, 0, 3, 1, 1)
    self.wis_label = QtGui.QLabel("Wisdom", self.summary_layout)
    self.wis_label.setAlignment(QtCore.Qt.AlignCenter)
    self.wis_label.setObjectName(_fromUtf8("wis_label"))
    self.ability_layout.addWidget(self.wis_label, 0, 4, 1, 1)
    self.cha_label = QtGui.QLabel("Charisma", self.summary_layout)
    self.cha_label.setAlignment(QtCore.Qt.AlignCenter)
    self.cha_label.setObjectName(_fromUtf8("cha_label"))
    self.ability_layout.addWidget(self.cha_label, 0, 5, 1, 1)
    self.str_label = QtGui.QLabel("Strength", self.summary_layout)
    self.str_label.setAlignment(QtCore.Qt.AlignCenter)
    self.str_label.setObjectName(_fromUtf8("str_label"))
    self.ability_layout.addWidget(self.str_label, 0, 0, 1, 1)
    self.str_value = QtGui.QLabel("12", self.summary_layout)
    self.str_value.setAlignment(QtCore.Qt.AlignCenter)
    self.str_value.setObjectName(_fromUtf8("str_value"))
    self.ability_layout.addWidget(self.str_value, 1, 0, 1, 1)
    self.dex_value = QtGui.QLabel("10", self.summary_layout)
    self.dex_value.setAlignment(QtCore.Qt.AlignCenter)
    self.dex_value.setObjectName(_fromUtf8("dex_value"))
    self.ability_layout.addWidget(self.dex_value, 1, 1, 1, 1)
    self.con_value = QtGui.QLabel("9", self.summary_layout)
    self.con_value.setAlignment(QtCore.Qt.AlignCenter)
    self.con_value.setObjectName(_fromUtf8("con_value"))
    self.ability_layout.addWidget(self.con_value, 1, 2, 1, 1)
    self.int_value = QtGui.QLabel("16", self.summary_layout)
    self.int_value.setAlignment(QtCore.Qt.AlignCenter)
    self.int_value.setObjectName(_fromUtf8("int_value"))
    self.ability_layout.addWidget(self.int_value, 1, 3, 1, 1)
    self.wis_value = QtGui.QLabel("8", self.summary_layout)
    self.wis_value.setAlignment(QtCore.Qt.AlignCenter)
    self.wis_value.setObjectName(_fromUtf8("wis_value"))
    self.ability_layout.addWidget(self.wis_value, 1, 4, 1, 1)
    self.cha_value = QtGui.QLabel("11", self.summary_layout)
    self.cha_value.setAlignment(QtCore.Qt.AlignCenter)
    self.cha_value.setObjectName(_fromUtf8("cha_value"))
    self.ability_layout.addWidget(self.cha_value, 1, 5, 1, 1)
    self.verticalLayout_17.addLayout(self.ability_layout)

    # proficiencies
    self.proficiencies_layout = QtGui.QGroupBox("Proficiencies", self.summary_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.proficiencies_layout.sizePolicy().hasHeightForWidth())
    self.proficiencies_layout.setSizePolicy(sizePolicy)
    self.proficiencies_layout.setObjectName(_fromUtf8("proficiencies_layout"))
    self.horizontalLayout_42 = QtGui.QHBoxLayout(self.proficiencies_layout)
    self.horizontalLayout_42.setObjectName(_fromUtf8("horizontalLayout_42"))
    
    self.saving_skill_layout = QtGui.QVBoxLayout()
    self.saving_skill_layout.setObjectName(_fromUtf8("saving_skill_layout"))

    # skill
    self.list_skill = []
    self.skill_layout = QtGui.QGroupBox("Skills", self.proficiencies_layout)
    self.skill_layout.setObjectName(_fromUtf8("skill_layout"))
    self.gridLayout_15 = QtGui.QGridLayout(self.skill_layout)
    self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
    self.saving_skill_layout.addWidget(self.skill_layout)

    # saving throws
    self.list_saving = []
    self.saving_layout = QtGui.QGroupBox("Saving Throws", self.proficiencies_layout)
    self.saving_layout.setObjectName(_fromUtf8("saving_layout"))
    self.hLayout_saving = QtGui.QHBoxLayout(self.saving_layout)
    self.hLayout_saving.setObjectName(_fromUtf8("hLayout_saving"))
    self.saving_skill_layout.addWidget(self.saving_layout)

    self.horizontalLayout_42.addLayout(self.saving_skill_layout)

    # right layout
    self.object_lang_prof_layout = QtGui.QVBoxLayout()

    # Object proficiencies
    self.list_object = []
    self.object_proficiency_layout = QtGui.QGroupBox("Objects", self.proficiencies_layout)
    self.object_proficiency_layout.setObjectName(_fromUtf8("object_proficiency_layout"))
    self.gridLayout_16 = QtGui.QGridLayout(self.object_proficiency_layout)
    self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
    self.object_lang_prof_layout.addWidget(self.object_proficiency_layout)

    # Language proficiencies
    self.list_lang = []
    self.lang_proficiency_layout = QtGui.QGroupBox("Languages", self.proficiencies_layout)
    self.lang_proficiency_layout.setObjectName(_fromUtf8("lang_proficiency_layout"))
    self.lang_gridLayout = QtGui.QGridLayout(self.lang_proficiency_layout)
    self.lang_gridLayout.setObjectName(_fromUtf8("lang_gridLayout"))
    self.object_lang_prof_layout.addWidget(self.lang_proficiency_layout)
    
    self.horizontalLayout_42.addLayout(self.object_lang_prof_layout)
    self.verticalLayout_17.addWidget(self.proficiencies_layout)
    self.horizontalLayout_2.addWidget(self.summary_layout)

    self.loadListCharacters()
