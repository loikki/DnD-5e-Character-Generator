# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/dnd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4


from PyQt4 import QtCore, QtGui
from string import lower
import pickle
import os

from core.character import Character
import core.background as background
import core.race as race
import core.dnd_class as dnd_class
import core.character as character
import core.spell as spell
import core.proficiency as proficiency
import core.trait as trait

import gui.player.tools as tools

from gui.player.setup_character_choice import setupCharacterChoice
from gui.player.setup_description import setupDescription
from gui.player.setup_background import setupBackground
from gui.player.setup_race import setupRace
from gui.player.setup_class import setupClass
from gui.player.setup_spell import setupSpell
from gui.player.setup_equipment import setupEquipment
from gui.player.setup_stat import setupStat

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class CharacterGenerator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1005, 719)
        MainWindow.setWindowTitle("Loikki's Character Generator")

        # by default, no character is loaded
        self.character = character.Character()
        self.background_parser = background.BackgroundParser()
        self.race_parser = race.RaceParser()
        self.class_parser = dnd_class.DnDClassParser()
        self.spell_parser = spell.SpellParser()
        self.trait_parser = trait.TraitParser()
        
        # Create main tab
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.main_tab = QtGui.QTabWidget(self.centralwidget)
        self.main_tab.setObjectName(_fromUtf8("main_tab"))

        # create each individual tabs
        setupCharacterChoice(self)
        setupDescription(self)
        setupRace(self)
        setupClass(self)
        setupSpell(self)
        setupBackground(self)
        setupEquipment(self)
        self.setupNotes()
        setupStat(self)

        # create toolbar
        self.horizontalLayout.addWidget(self.main_tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionPrint = QtGui.QAction("Print", MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionPrint.triggered.connect(self.printCharacter)

        self.actionSave = QtGui.QAction("Save", MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.triggered.connect(self.saveCharacter)
        
        self.actionQuit = QtGui.QAction("Quit", MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionQuit)

    # ------------------ ACTION ---------------------------------------
    
    # tool bar
    def saveCharacter(self):
        pickle.dump(self.character, open(
            os.path.join("data", "saved", "player", self.character.name + ".p"), 'wb'))

    def printCharacter(self):
        print "Not implemented yet"

    def initializeCharacter(self, new):
        """ 
        :param bool new: Is a new character?
        """
        return
    
    # character choice tab
    def newCharacter(self):
        self.character = Character()
        self.initializeCharacter(True)
        
    def loadCharacter(self):
        character = self.tab0_character_choice.currentItem().text()
        for c in self.list_character:
            if character == c.name:
                character = c
                break
        self.character = character
        self.initializeCharacter(True)
        
    # description tab
    def importImage(self):
        openfile = QtGui.QFileDialog.getOpenFileName(self.centralwidget) # Filename line
        self.tab1_img.setPixmap(QtGui.QPixmap(openfile))
        f = open(openfile, 'r') # New line
        self.character.image = f.read() # New line

    def removeImage(self):
        self.character.image = None
        self.tab1_img.clear()

    # --------------- Character Choice ------------------------------------

    def loadListCharacters(self):
        if self.main_tab.currentIndex() != 0:
            return
        self.list_character = []
        character_directory = os.path.join("data", "saved", "player", "")
        for character_file in os.listdir(character_directory):
            self.list_character.append(pickle.load(
                open(character_directory + character_file, 'rb')))
        for character in self.list_character:
            self.tab0_character_choice.addItem(character.name)

    def printSummary(self):
        character = self.tab0_character_choice.currentItem().text()
        for c in self.list_character:
            if character == c.name:
                character = c
                break

        self.tab0_raceLineEdit.setText(character.race.subrace_name)
        self.tab0_classLineEdit.setText(character.dnd_class.class_name)
        self.tab0_specializationLineEdit.setText(
            character.dnd_class.specialization_name)
        self.tab0_backgroundLineEdit.setText(
            character.background.background_name)
        self.tab0_experienceLevelLineEdit.setText(
            str(character.experience))
        self.tab0_str_value.setText(str(character.getStrength()))
        self.tab0_dex_value.setText(str(character.getDexterity()))
        self.tab0_con_value.setText(str(character.getConstitution()))
        self.tab0_int_value.setText(str(character.getIntelligence()))
        self.tab0_wis_value.setText(str(character.getWisdom()))
        self.tab0_cha_value.setText(str(character.getCharisma()))
        self.character.background.getProficiency(None)
        self.loadProficiency(character)


    def loadProficiency(self, character):
        for i in range(len(self.tab0_list_skill)):
            self.gridLayout_15.removeWidget(self.tab0_list_skill[i])
            self.tab0_list_skill[i].deleteLater()

        self.tab0_list_skill = []
        # skills
        prof = character.getProficiency()
        skills = prof.skills
        j = 0
        for i in range(len(skills)):
            if skills[i]:
                label = QtGui.QLabel(
                    tools.choiceLabel(proficiency.SkillProficiency(i).name),
                    self.tab0_skill_layout)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.gridLayout_15.addWidget(label, int(j/2), j%2)
                self.tab0_list_skill.append(label)
                j += 1

        # Saving
        saving = prof.saving
        for i in range(len(self.tab0_list_saving)):
            self.hLayout_saving.removeWidget(self.tab0_list_saving[i])
            self.tab0_list_saving[i].deleteLater()
        self.tab0_list_saving = []

        for i in range(len(saving)):
            if saving[i]:
                label = QtGui.QLabel(
                    tools.choiceLabel(proficiency.Ability(i).name),
                    self.tab0_saving_layout)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.hLayout_saving.addWidget(label)
                self.tab0_list_saving.append(label)

        # Object
        for i in range(len(self.tab0_list_object)):
            self.gridLayout_16.removeWidget(self.tab0_list_object[i])
            self.tab0_list_object[i].deleteLater()
        self.tab0_list_object = []
        weapon = prof.weapons
        j = tools.createObjectProficiencyLabel(
            self, weapon, proficiency.WeaponProficiency)
        tool = prof.tools
        j = tools.createObjectProficiencyLabel(
            self, tool, proficiency.ToolProficiency, j)
        armor = prof.armors
        j = tools.createObjectProficiencyLabel(
            self, armor, proficiency.ArmorProficiency, j)   

        # TODO add groupBox for languages
        lang = prof.languages
        
    # --------------- DESCRIPTION FUNCTIONS -------------------------------
        
    def rollAbilities(self):
        """ Roll 6 times 4d6 and remove the lowest one
        """
        if self.tab1_ability_style_combo.currentText() != 'Random':
            return
        roll = tools.rollAbility()
        self.tab1_ability_value_1.setText(str(roll))
        roll = tools.rollAbility()
        self.tab1_ability_value_2.setText(str(roll))
        roll = tools.rollAbility()
        self.tab1_ability_value_3.setText(str(roll))
        roll = tools.rollAbility()
        self.tab1_ability_value_4.setText(str(roll))
        roll = tools.rollAbility()
        self.tab1_ability_value_5.setText(str(roll))
        roll = tools.rollAbility()
        self.tab1_ability_value_6.setText(str(roll))
        self.character.dnd_class.getProficiency(None)
        self.character.write()

    def changeRollStyle(self, style):
        self.tab1_ability_value_1.clear()
        self.tab1_ability_value_2.clear()
        self.tab1_ability_value_3.clear()
        self.tab1_ability_value_4.clear()
        self.tab1_ability_value_5.clear()
        self.tab1_ability_value_6.clear()
        self.tab1_ability_point_score.clear()
        if style == 'Free' or style == 'Points':
            self.tab1_ability_value_1.setReadOnly(False)
            self.tab1_ability_value_2.setReadOnly(False)
            self.tab1_ability_value_3.setReadOnly(False)
            self.tab1_ability_value_4.setReadOnly(False)
            self.tab1_ability_value_5.setReadOnly(False)
            self.tab1_ability_value_6.setReadOnly(False)
        else:
            self.tab1_ability_value_1.setReadOnly(True)
            self.tab1_ability_value_2.setReadOnly(True)
            self.tab1_ability_value_3.setReadOnly(True)
            self.tab1_ability_value_4.setReadOnly(True)
            self.tab1_ability_value_5.setReadOnly(True)
            self.tab1_ability_value_6.setReadOnly(True)
        if  style == 'Pregenerated':
            self.tab1_ability_value_1.setText("15")
            self.tab1_ability_value_2.setText("14")
            self.tab1_ability_value_3.setText("13")
            self.tab1_ability_value_4.setText("12")
            self.tab1_ability_value_5.setText("10")
            self.tab1_ability_value_6.setText("8")
        elif style == 'Points':
            self.tab1_ability_value_1.setText("8")
            self.tab1_ability_value_2.setText("8")
            self.tab1_ability_value_3.setText("8")
            self.tab1_ability_value_4.setText("8")
            self.tab1_ability_value_5.setText("8")
            self.tab1_ability_value_6.setText("8")
        

    def notableFeaturesChanged(self):
        features = self.tab1_features.toPlainText()
        self.character.notable_features = features

    def changeAbilityRoll(self):
        self.tab1_ability_point_score.clear()
        if self.tab1_ability_style_combo.currentText() == 'Points':
            points = 0
            list_ability_value = [self.tab1_ability_value_1, self.tab1_ability_value_2,
                                  self.tab1_ability_value_3, self.tab1_ability_value_4,
                                  self.tab1_ability_value_5, self.tab1_ability_value_6]
            for value in list_ability_value:
                if value.text() == '':
                    return
                temp = int(value.text())
                if temp < 8 or temp > 15:
                    points = float('nan')
                elif temp == 9:
                    points += 1
                elif temp == 10:
                    points += 2
                elif temp == 11:
                    points += 3
                elif temp == 12:
                    points += 4
                elif temp == 13:
                    points += 5
                elif temp == 14:
                    points += 7
                elif temp == 15:
                    points += 9
            self.tab1_ability_point_score.setText(str(points) + "/27 Points Used")
        list_ability = [self.tab1_str_combo, self.tab1_dex_combo, self.tab1_con_combo,
                        self.tab1_int_combo, self.tab1_wis_combo, self.tab1_cha_combo]
        for combo in list_ability:
            combo.clear()
        self.changeAttributionAbility(None)

    def changeAttributionAbility(self, not_used):
        list_ability = [self.tab1_str_combo, self.tab1_dex_combo, self.tab1_con_combo,
                        self.tab1_int_combo, self.tab1_wis_combo, self.tab1_cha_combo]
        list_value = [self.tab1_ability_value_1.text(), self.tab1_ability_value_2.text(),
                      self.tab1_ability_value_3.text(), self.tab1_ability_value_4.text(),
                      self.tab1_ability_value_5.text(), self.tab1_ability_value_6.text()]
        for combo in list_ability:
            if combo.currentText() != '':
                list_value.remove(combo.currentText())
        for combo in list_ability:
            temp = combo.currentText()
            combo.clear()
            if temp != '':
                combo.addItem(temp)
            combo.addItem("")
            for i in range(len(list_value)):
                combo.addItem(list_value[i])
        
    # --------------- RACE FUNCTIONS --------------------------------------
    def changeRace(self, race):
        """ Action that will be done when the user change the race
        """
        self.tab2_race_description.setText(self.race_parser.getDescription(race))
        self.updateSubrace()
        self.character.race.setRace(race)

    def updateSubrace(self):
        """ Update the list of subrace
        """
        race = self.tab2_race_choice_combo.currentText()
        self.tab2_subrace_choice_combo.clear()
        for i in self.race_parser.getListSubrace(race):
            self.tab2_subrace_choice_combo.addItem(i)
        self.changeSubrace(self.tab2_subrace_choice_combo.currentText())
        
    def changeSubrace(self, subrace):
        race = self.tab2_race_choice_combo.currentText()
        self.tab2_subrace_description.setText(
            self.race_parser.getSubraceDescription(race, subrace))
        self.changeRaceTabChoice()
        self.character.race.setSubrace(subrace)

    def changeRaceTabChoice(self):
        """ Update the race choice widgets
        :param str background: race name
        """
        race = self.tab2_race_choice_combo.currentText()
        subrace = self.tab2_subrace_choice_combo.currentText()
        list_choice = self.race_parser.getChoice(race)
        list_choice.extend(self.race_parser.getSubraceChoice(race, subrace))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.tab2_choice_list)):
            # delete spacer
            if i == 0 or (i == len(self.tab2_choice_list)-1 and i==3):
                self.tab2_choices_layout.removeItem(self.tab2_choice_list[i])
            else:
                self.tab2_choices_layout.removeWidget(self.tab2_choice_list[i])
                self.tab2_choice_list[i].deleteLater()
        self.tab2_choice_list = []

        j = 0
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.tab2_choice_list.append(spacer)
        self.tab2_choices_layout.addItem(spacer, int(j/4), j%4)
        for choice in list_choice:
            for i in range(choice[2]):
                j += 1
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.tab2)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.tab2_choices_layout.addWidget(label, int(j/4), j%4)
                self.tab2_choice_list.append(label)
                j += 1
                combo = QtGui.QComboBox(self.tab2)
                combo.activated.connect(self.makeRaceChoice)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                self.tab2_choices_layout.addWidget(combo, int(j/4), j%4)
                self.tab2_choice_list.append(combo)

        if j < 3:
            j += 1
            spacer1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.tab2_choice_list.append(spacer1)
            self.tab2_choices_layout.addItem(spacer1, int(j/4), j%4)


    def makeRaceChoice(self, useless):
        """ Update the list of choice in the character's race
        """
        choice = []
        for i in range(len(self.tab2_choice_list)):
            if i%2 == 0 and i!=0:
                choice.append(str(self.tab2_choice_list[i].currentText()))
                
        self.character.race.choice = choice
            

    # --------------- CLASS FUNCTIONS --------------------------------------

    def changeClass(self, dnd_class):
        """ Action that will be done when the user change the class
        :param str dnd_class: class in the combo box
        """
        self.tab3_class_description.setText(self.class_parser.getDescription(dnd_class))
        self.updateSpecialization()
        self.character.dnd_class.class_name = dnd_class

    def updateSpecialization(self):
        """ Update the list of specialization
        """
        dnd_class = self.tab3_class_combo.currentText()
        self.tab3_specialization_combo.clear()
        for i in self.class_parser.getListSpecialization(dnd_class):
            self.tab3_specialization_combo.addItem(i)
        self.changeSpecialization(self.tab3_specialization_combo.currentText())
        
    def changeSpecialization(self, specialization):
        """ Action that will be done when the user change the specialization
        :param str specialization: specialization selected
        """
        dnd_class = self.tab3_class_combo.currentText()
        self.tab3_specialization_description.setText(
            self.class_parser.getSpecializationDescription(dnd_class, specialization))
        self.changeClassTabChoice()
        self.character.dnd_class.specialization_name = specialization

    def changeClassTabChoice(self):
        """ Update the class choice widgets
        """
        dnd_class = self.tab3_class_combo.currentText()
        specialization = self.tab3_specialization_combo.currentText()
        list_choice = self.class_parser.getChoice(dnd_class)
        list_choice.extend(self.class_parser.getSpecializationChoice(dnd_class, specialization))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.tab3_choice_list)):
            if (i == 0) or (i == len(self.tab3_choice_list)-1):
                self.tab3_choices_layout.removeItem(self.tab3_choice_list[i])
            else:
                self.tab3_choices_layout.removeWidget(self.tab3_choice_list[i])
                self.tab3_choice_list[i].deleteLater()

        self.tab3_choice_list = []

        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.tab3_choice_list.append(spacer)
        self.tab3_choices_layout.addItem(spacer)
        j = 0
        for choice in list_choice:
            for i in range(choice[2]):
                j += 1
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.tab3)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.tab3_choices_layout.addWidget(label, j, 0)
                self.tab3_choice_list.append(label)
                combo = QtGui.QComboBox(self.tab3)
                combo.activated[str].connect(self.makeClassChoice)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                self.tab3_choices_layout.addWidget(combo, j, 1)
                self.tab3_choice_list.append(combo)

        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.tab3_choice_list.append(spacer)
        self.tab3_choices_layout.addItem(spacer)

    def makeClassChoice(self, useless):
        """ Update the list of choice in the character's background
        """
        choice = []
        for i in range(len(self.tab3_choice_list)):
            if i%2 == 0 and i!=0:
                choice.append(str(self.tab3_choice_list[i].currentText()))
                
        self.character.dnd_class.choice = choice

    # --------------- BACKGROUND FUNCTIONS ---------------------------------
        
    def changeBackground(self, background):
        """ action that will be done when the user change the background
        :param str background: New background
        """
        self.tab5_ideal_combo.clear()
        self.tab5_background_description.setText(
            self.background_parser.getDescription(background))
        perso_max = self.background_parser.getNumberPersonality(background)
        self.tab5_personality_spinbox_1.setMaximum(perso_max)
        self.tab5_personality_spinbox_2.setMaximum(perso_max)
        flaw_max = self.background_parser.getNumberFlaw(background)
        self.tab5_flaw_spinbox.setMaximum(flaw_max)
        bond_max = self.background_parser.getNumberBond(background)
        self.tab5_bond_spinbox.setMaximum(bond_max)
        for ideal in self.background_parser.getListIdeal(background):
            self.tab5_ideal_combo.addItem(ideal)
        self.changeBackgroundChoice(background)
        self.character.background.setBackgroundName(background)

        
    def changeIdealDescription(self, ideal):
        """ Update the text of the ideal
        :param str ideal: New Ideal
        """
        background = self.tab5_background_combo.currentText()
        self.tab5_ideal_description.setText(
            self.background_parser.getIdealDescription(background, ideal))
        self.character.background.setIdeal(ideal)

    def changePersonalityDescription(self, personality):
        """ Update the description text of the personality
        :param personality: Not used (present due to Qt)
        """
        background = self.tab5_background_combo.currentText()
        perso1 = self.tab5_personality_spinbox_1.value()
        perso2 = self.tab5_personality_spinbox_2.value()
        if perso1 == perso2:
            self.tab5_personality_description.setText(
                "Please choose two different personalities!")
            return
        self.character.background.setPersonality0(perso1)
        self.character.background.setPersonality1(perso2)
        perso1 = self.background_parser.getPersonalityDescription(
            background, perso1)
        perso2 = self.background_parser.getPersonalityDescription(
            background, perso2)
        text = "<p>" + perso1 + "</p> <p>" + perso2 + "</p>"
        self.tab5_personality_description.setText(text)

    def changeBackgroundChoice(self, background):
        """ Update the background choice widgets
        :param str background: Background name
        """
        list_choice = self.background_parser.getChoice(background)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.tab5_choice_list)):
            # delete spacer
            if i%3 == 0:
                self.horizontalLayout_33.removeItem(self.tab5_choice_list[i])
            # delete widget
            else:
                self.horizontalLayout_33.removeWidget(self.tab5_choice_list[i])
                self.tab5_choice_list[i].deleteLater()
                
        self.tab5_choice_list = []
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.tab5_choice_list.append(spacer)
        self.horizontalLayout_33.addItem(spacer)
        for choice in list_choice:
            for i in range(choice[2]):
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.tab5_choice_layout)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_33.addWidget(label)
                self.tab5_choice_list.append(label)
                combo = QtGui.QComboBox(self.tab5_choice_layout)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                combo.activated[str].connect(self.makeBackgroundChoice)
                self.horizontalLayout_33.addWidget(combo)
                self.tab5_choice_list.append(combo)
                spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                self.tab5_choice_list.append(spacer)
                self.horizontalLayout_33.addItem(spacer)

    def makeBackgroundChoice(self, useless):
        """ Update the list of choice in the character's background
        """
        choice = []
        for i in range(len(self.tab5_choice_list)):
            if i%3 == 2:
                choice.append(str(self.tab5_choice_list[i].currentText()))
                
        self.character.background.choice = choice
        
    def changeFlawDescription(self, flaw):
        """ Update the description of the flaw
        :param int flaw: value of the flaw
        """
        background = self.tab5_background_combo.currentText()
        self.tab5_flaw_description.setText(
            self.background_parser.getFlawDescription(background, flaw))
        self.character.background.setFlaw(flaw)

    def changeBondDescription(self, bond):
        """ Update the description of the bond
        :param int bond: value of the bond
        """
        background = self.tab5_background_combo.currentText()
        self.tab5_bond_description.setText(
            self.background_parser.getBondDescription(background, bond))
        self.character.background.setBond(bond)
        
    def fullRandomBackground(self):
        """ Choose randomly the background, personality, ideal, bond
        and flaw of the character
        """
        nber_background = len(self.background_parser.getListBackground())
        self.tab5_background_combo.setCurrentIndex(
            tools.rollDice(1, nber_background) - 1)
        background = self.tab5_background_combo.currentText()
        self.changeBackground(background)
        self.randomPersonality()

    def randomPersonality(self):
        """ Choose the personality of the character (bond, flaw, ideal,
        personality)
        """
        background = self.tab5_background_combo.currentText()
        nber_perso = self.background_parser.getNumberPersonality(background)
        nber_flaw = self.background_parser.getNumberFlaw(background)
        nber_bond = self.background_parser.getNumberBond(background)
        nber_ideal = len(self.background_parser.getListIdeal(background))
        # bond
        self.tab5_bond_spinbox.setValue(tools.rollDice(1, nber_bond))
        # flaw
        self.tab5_flaw_spinbox.setValue(tools.rollDice(1, nber_flaw))
        # personality
        roll1 = tools.rollDice(1, nber_perso)
        self.tab5_personality_spinbox_1.setValue(roll1)
        roll2 = tools.rollDice(1, nber_perso - 1)
        if roll2 >= roll1:
            roll2 += 1
        self.tab5_personality_spinbox_2.setValue(roll2)
        # ideal
        self.tab5_ideal_combo.setCurrentIndex(tools.rollDice(1, nber_ideal)-1)
        ideal = self.tab5_ideal_combo.currentText()
        self.changeIdealDescription(ideal)

        # alignment
        align = self.background_parser.getIdealAlignement(background, ideal)
        if lower(align) == 'any':
            self.tab5_alignment_combo.setCurrentIndex(tools.rollDice(1,9)-1)
        else:
            index_align = []
            for i in range(9):
                if lower(align) in lower(str(self.tab5_alignment_combo.itemText(i))):
                    index_align.append(i)
            roll = tools.rollDice(1,len(index_align))-1
            self.tab5_alignment_combo.setCurrentIndex(index_align[roll])
        self.character.background.setAlignment(
            self.tab5_alignment_combo.currentText())

    # --------------------------- SPELL -------------------------------

    def updateSpellDescription(self, value):
        """
        :param QTreeWidgetItem value: Spell name
        """
            
        if value is None or value.childCount() != 0:
            self.tab4_tab1_description.clear()
            return
        description = self.spell_parser.getDescription(value.text(0))
        self.tab4_tab1_description.setText(description)
        
        
    def updateCantripDescription(self, value):
        """
        :param QTreeWidgetItem value: Cantrip name
        """
        if value is None or value.childCount() != 0:
            self.tab4_tab0_description.clear()
            return
        description = self.spell_parser.getDescription(value.text(0))
        self.tab4_tab0_description.setText(description)
        
    
    def selectClassSpell(self, value):
        """ Update the list of spell and show only the spell of the given class
        :param str value: Class name
        """
        self.tab4_tab0_class_combo.setCurrentIndex(
            self.tab4_tab0_class_combo.findText(value))
        self.tab4_tab1_class_combo.setCurrentIndex(
            self.tab4_tab1_class_combo.findText(value))
        value = lower(str(value))
        if value == 'any':
            value = None
        self.tab4_tab0_list_tree.clear()
        self.tab4_tab1_list_tree.clear()
        self.tab4_tab1_lvl_1 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["1st Level"])
        self.tab4_tab1_lvl_2 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["2nd Level"])
        self.tab4_tab1_lvl_3 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["3rd Level"])
        self.tab4_tab1_lvl_4 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["4th Level"])
        self.tab4_tab1_lvl_5 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["5th Level"])
        self.tab4_tab1_lvl_6 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["6th Level"])
        self.tab4_tab1_lvl_7 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["7th Level"])
        self.tab4_tab1_lvl_8 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["8th Level"])
        self.tab4_tab1_lvl_9 = QtGui.QTreeWidgetItem(self.tab4_tab1_list_tree, ["9th Level"])
        for i in self.spell_parser.getListSpell(0, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab0_list_tree, i)
        for i in self.spell_parser.getListSpell(1, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_1, i)
        for i in self.spell_parser.getListSpell(2, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_2, i)
        for i in self.spell_parser.getListSpell(3, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_3, i)
        for i in self.spell_parser.getListSpell(4, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_4, i)
        for i in self.spell_parser.getListSpell(5, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_5, i)
        for i in self.spell_parser.getListSpell(6, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_6, i)
        for i in self.spell_parser.getListSpell(7, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_7, i)
        for i in self.spell_parser.getListSpell(8, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_8, i)
        for i in self.spell_parser.getListSpell(9, value):
            item = QtGui.QTreeWidgetItem(self.tab4_tab1_lvl_9, i)

    def _findLevelItemKnownSpell(self, level_text):
        """
        :param str level_text:
        :returns: QTreeWidgetItem
        """
        spell_tree = None
        if "1" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("1st Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["1st Level"])
            else:
                spell_tree = spell_tree[0]
        elif "2" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("2nd Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["2nd Level"])
            else:
                spell_tree = spell_tree[0]
        elif "3" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("3rd Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["3rd Level"])
            else:
                spell_tree = spell_tree[0]
        elif "4" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("4th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["4th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "5" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("5th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["5th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "6" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("6th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["6th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "7" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("7th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["7th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "8" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("8th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["8th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "9" in level_text:
            spell_tree = self.tab4_tab1_known_tree.findItems("9th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab4_tab1_known_tree, ["9th Level"])
            else:
                spell_tree = spell_tree[0]
        return spell_tree

    def addSpell(self):
        item = self.tab4_tab1_list_tree.currentItem()
        level = self.tab4_tab1_known_tree.findItems("Level", QtCore.Qt.MatchContains, 0)
        matches = []
        for i in level:
            for k in range(i.childCount()):
                child = i.child(k)
                if child.text(0) == item.text(0):
                    matches.append(child.text(0))
        if item.childCount() != 0 or len(matches) != 0:
            return
        spell = []
        spell_tree = self._findLevelItemKnownSpell(item.parent().text(0))

        for i in range(item.columnCount()):
            spell.append(item.text(i))
        QtGui.QTreeWidgetItem(spell_tree, spell)
        

    def removeSpell(self):
        item = self.tab4_tab1_known_tree.currentItem()
        parent = item.parent()
        parent.removeChild(item)
        if parent.childCount() == 0:
            index = parent.treeWidget().indexOfTopLevelItem(parent)
            parent.treeWidget().takeTopLevelItem(index)
    
    def addCantrip(self):
        item = self.tab4_tab0_list_tree.currentItem()
        matches = self.tab4_tab0_known_tree.findItems(item.text(0), QtCore.Qt.MatchFixedString, 0)
        if item.childCount() != 0 or len(matches) != 0:
            return
        cantrip = []
        for i in range(item.columnCount()):
            cantrip.append(item.text(i))
        QtGui.QTreeWidgetItem(self.tab4_tab0_known_tree, cantrip)
        
    def removeCantrip(self):
        item = self.tab4_tab0_known_tree.currentItem()
        index = item.treeWidget().indexOfTopLevelItem(item)
        item.treeWidget().takeTopLevelItem(index)

    def updateTrait(self):
        if (self.tab4_spell_tab.currentIndex() != 2 and
            self.main_tab.currentIndex() != 8):
            return
        race = self.character.race.race_name
        subrace = self.character.race.subrace_name
        trait = self.race_parser.getTrait(race, subrace)
        self.tab4_tab2_tree.clear()
        self.tab8_trait_tree.clear()

        for i in trait:
            max_use = self.trait_parser.getMaxUse(i.get('name'))
            if max_use is None:
                max_use = ''
            item = QtGui.QTreeWidgetItem(self.tab4_tab2_tree,
                                         [i.get('name'), max_use])
            item = QtGui.QTreeWidgetItem(self.tab8_trait_tree,
                                         [i.get('name'), max_use])

    def updateTraitDescription(self, value):
        if value is None:
            self.tab4_tab2_description.clear()
            return
        description = self.trait_parser.getDescription(value.text(0))
        self.tab4_tab2_description.setText(description)

    # --------------------------- STAT --------------------------------

    def updateStatList(self):
        if self.main_tab.currentIndex() != 8:
            return
        # trait
        self.updateTrait()

        self.tab8_spell_tree.clear()
        # cantrip
        root = self.tab4_tab0_known_tree.invisibleRootItem()
        cantrip = QtGui.QTreeWidgetItem(self.tab8_spell_tree, ["Cantrip"])
        for i in range(root.childCount()):
            item = root.child(i).clone()
            cantrip.addChild(item)
            
        # spell
        root = self.tab4_tab1_known_tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i).clone()
            self.tab8_spell_tree.invisibleRootItem().addChild(item)                

        
    # --------------------------- GUI ---------------------------------                    
        
        
    def setupNotes(self):
        self.tab7 = QtGui.QWidget()
        self.tab7.setObjectName(_fromUtf8("tab7"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.tab7)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.tab7_notes = QtGui.QPlainTextEdit(self.tab7)
        self.tab7_notes.setObjectName(_fromUtf8("tab7_notes"))
        self.horizontalLayout_21.addWidget(self.tab7_notes)
        self.main_tab.addTab(self.tab7, "Notes")
