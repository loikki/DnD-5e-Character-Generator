# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/dnd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4


from PyQt4 import QtCore, QtGui
from string import lower
import pickle
import os, sys

from core.character import Character
import core.background as background
import core.race as race
import core.dnd_class as dnd_class
import core.character as character
import core.proficiency as proficiency

import gui.tools as tools

from gui.player.setup_description import setupDescription
from gui.player.setup_background import setupBackground
from gui.player.setup_race import setupRace
from gui.player.setup_class import setupClass

class CharacterGeneratorWizard(QtGui.QWizard):
    def __init__(self):
        super(QtGui.QWizard, self).__init__()
        self.character = character.Character()
        
    def validateCurrentPage(self):
        if self.currentPage().isFinalPage():
            if not self.character.getProficiency()[1]:
                prof = self.character.dnd_class.getProficiency()[0]
                prof = self.character.background.getProficiency(None, prof)[0]
                prof = self.character.race.getProficiency(None, prof)[0]
                dict_prof = prof.getProficiency()
                question = """You have choosen twice the same
proficiency, please modify them:\n """
                for i in dict_prof.keys():
                    question += "\n" + i + ":\n "
                    for j in dict_prof[i]:
                        question += j + "\n "
                QtGui.QMessageBox.question(
                    self, 'Message',
                    question, QtGui.QMessageBox.Ok,
                    QtGui.QMessageBox.Ok)
                return False
        return True

class CharacterGenerator(object):
    def setupUi(self, mainWindow):
        self.mainWindow = mainWindow
        self.wizard = CharacterGeneratorWizard()
        self.wizard.setObjectName(tools._fromUtf8("Character Generator"))
        self.wizard.resize(1005, 719)
        self.wizard.setWindowTitle("Character Generator")

        # by default, no character is loaded
        self.background_parser = background.BackgroundParser()
        self.race_parser = race.RaceParser()
        self.class_parser = dnd_class.DnDClassParser()


        # create each individual tabs
        self.wizard.addPage(setupDescription(self))
        self.wizard.addPage(setupRace(self))
        self.wizard.addPage(setupClass(self))
        self.wizard.addPage(setupBackground(self))
        self.wizard.addPage(self.setupNotes())
        

        self.wizard.accepted.connect(self.saveCharacter)
        self.wizard.show()

    # ------------------ ACTION ---------------------------------------
    
    # tool bar
    def saveCharacter(self):
        self.wizard.character.setHitPoint()
        pickle.dump(self.wizard.character, open(
            os.path.join("data", "saved", "player", self.wizard.character.name + ".p"), 'wb'))
        self.mainWindow.loadListCharacters()
        
    # description tab
    def importImage(self):
        openfile = QtGui.QFileDialog.getOpenFileName(self.wizard) # Filename line
        self.page0_img.setPixmap(QtGui.QPixmap(openfile))
        f = open(openfile, 'r')
        self.wizard.character.image = f.read()

    def removeImage(self):
        self.wizard.character.image = None
        self.page0_img.clear()

        
    # --------------- DESCRIPTION FUNCTIONS -------------------------------
        
    def rollAbilities(self):
        """ Roll 6 times 4d6 and remove the lowest one
        """
        if self.page0_ability_style_combo.currentText() != 'Random':
            return
        roll = tools.rollAbility()
        self.page0_ability_value_1.setText(str(roll))
        roll = tools.rollAbility()
        self.page0_ability_value_2.setText(str(roll))
        roll = tools.rollAbility()
        self.page0_ability_value_3.setText(str(roll))
        roll = tools.rollAbility()
        self.page0_ability_value_4.setText(str(roll))
        roll = tools.rollAbility()
        self.page0_ability_value_5.setText(str(roll))
        roll = tools.rollAbility()
        self.page0_ability_value_6.setText(str(roll))

    def changeRollStyle(self, style):
        self.page0_ability_value_1.clear()
        self.page0_ability_value_2.clear()
        self.page0_ability_value_3.clear()
        self.page0_ability_value_4.clear()
        self.page0_ability_value_5.clear()
        self.page0_ability_value_6.clear()
        self.page0_ability_point_score.clear()
        if style == 'Free' or style == 'Points':
            self.page0_ability_value_1.setReadOnly(False)
            self.page0_ability_value_2.setReadOnly(False)
            self.page0_ability_value_3.setReadOnly(False)
            self.page0_ability_value_4.setReadOnly(False)
            self.page0_ability_value_5.setReadOnly(False)
            self.page0_ability_value_6.setReadOnly(False)
        else:
            self.page0_ability_value_1.setReadOnly(True)
            self.page0_ability_value_2.setReadOnly(True)
            self.page0_ability_value_3.setReadOnly(True)
            self.page0_ability_value_4.setReadOnly(True)
            self.page0_ability_value_5.setReadOnly(True)
            self.page0_ability_value_6.setReadOnly(True)
        if  style == 'Pregenerated':
            self.page0_ability_value_1.setText("15")
            self.page0_ability_value_2.setText("14")
            self.page0_ability_value_3.setText("13")
            self.page0_ability_value_4.setText("12")
            self.page0_ability_value_5.setText("10")
            self.page0_ability_value_6.setText("8")
        elif style == 'Points':
            self.page0_ability_value_1.setText("8")
            self.page0_ability_value_2.setText("8")
            self.page0_ability_value_3.setText("8")
            self.page0_ability_value_4.setText("8")
            self.page0_ability_value_5.setText("8")
            self.page0_ability_value_6.setText("8")
        

    def notableFeaturesChanged(self):
        features = self.page0_features.toPlainText()
        self.wizard.character.notable_features = features

    def changeAbilityRoll(self):
        self.page0_ability_point_score.clear()
        if self.page0_ability_style_combo.currentText() == 'Points':
            points = 0
            list_ability_value = [self.page0_ability_value_1, self.page0_ability_value_2,
                                  self.page0_ability_value_3, self.page0_ability_value_4,
                                  self.page0_ability_value_5, self.page0_ability_value_6]
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
            self.page0_ability_point_score.setText(str(points) + "/27 Points Used")
        list_ability = [self.page0_str_combo, self.page0_dex_combo, self.page0_con_combo,
                        self.page0_int_combo, self.page0_wis_combo, self.page0_cha_combo]
        for combo in list_ability:
            combo.clear()
        self.changeAttributionAbility(None)

    def changeAttributionAbility(self, not_used):
        list_ability = [self.page0_str_combo, self.page0_dex_combo, self.page0_con_combo,
                        self.page0_int_combo, self.page0_wis_combo, self.page0_cha_combo]
        list_value = [self.page0_ability_value_1.text(), self.page0_ability_value_2.text(),
                      self.page0_ability_value_3.text(), self.page0_ability_value_4.text(),
                      self.page0_ability_value_5.text(), self.page0_ability_value_6.text()]
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
        self.page1_race_description.setText(self.race_parser.getDescription(race))
        self.updateSubrace()
        self.wizard.character.race.setRace(race)

    def updateSubrace(self):
        """ Update the list of subrace
        """
        race = self.page1_race_choice_combo.currentText()
        self.page1_subrace_choice_combo.clear()
        for i in self.race_parser.getListSubrace(race):
            self.page1_subrace_choice_combo.addItem(i)
        self.changeSubrace(self.page1_subrace_choice_combo.currentText())
        
    def changeSubrace(self, subrace):
        race = self.page1_race_choice_combo.currentText()
        self.page1_subrace_description.setText(
            self.race_parser.getSubraceDescription(race, subrace))
        self.changeRaceTabChoice()
        self.wizard.character.race.setSubrace(subrace)

    def changeRaceTabChoice(self):
        """ Update the race choice widgets
        :param str background: race name
        """
        race = self.page1_race_choice_combo.currentText()
        subrace = self.page1_subrace_choice_combo.currentText()
        list_choice = self.race_parser.getChoice(race)
        list_choice.extend(self.race_parser.getSubraceChoice(race, subrace))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.page1_choice_list)):
            # delete spacer
            if i == 0 or (i == len(self.page1_choice_list)-1 and i==3):
                self.page1_choices_layout.removeItem(self.page1_choice_list[i])
            else:
                self.page1_choices_layout.removeWidget(self.page1_choice_list[i])
                self.page1_choice_list[i].deleteLater()
        self.page1_choice_list = []

        j = 0
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.page1_choice_list.append(spacer)
        self.page1_choices_layout.addItem(spacer, int(j/4), j%4)
        for choice in list_choice:
            for i in range(choice[2]):
                j += 1
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.page1)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.page1_choices_layout.addWidget(label, int(j/4), j%4)
                self.page1_choice_list.append(label)
                j += 1
                combo = QtGui.QComboBox(self.page1)
                combo.activated.connect(self.makeRaceChoice)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                self.page1_choices_layout.addWidget(combo, int(j/4), j%4)
                self.page1_choice_list.append(combo)

        if j < 3:
            j += 1
            spacer1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.page1_choice_list.append(spacer1)
            self.page1_choices_layout.addItem(spacer1, int(j/4), j%4)

        self.makeRaceChoice(None)


    def makeRaceChoice(self, useless):
        """ Update the list of choice in the character's race
        """
        choice = []
        for i in range(len(self.page1_choice_list)):
            if i%2 == 0 and i!=0:
                choice.append(str(self.page1_choice_list[i].currentText()))
                
        self.wizard.character.race.choice = choice
            

    # --------------- CLASS FUNCTIONS --------------------------------------

    def changeClass(self, dnd_class):
        """ Action that will be done when the user change the class
        :param str dnd_class: class in the combo box
        """
        self.page2_class_description.setText(self.class_parser.getDescription(dnd_class))
        self.updateSpecialization()
        self.wizard.character.dnd_class.class_name = dnd_class

    def updateSpecialization(self):
        """ Update the list of specialization
        """
        dnd_class = self.page2_class_combo.currentText()
        self.page2_specialization_combo.clear()
        for i in self.class_parser.getListSpecialization(dnd_class):
            self.page2_specialization_combo.addItem(i)
        self.changeSpecialization(self.page2_specialization_combo.currentText())
        
    def changeSpecialization(self, specialization):
        """ Action that will be done when the user change the specialization
        :param str specialization: specialization selected
        """
        dnd_class = self.page2_class_combo.currentText()
        self.page2_specialization_description.setText(
            self.class_parser.getSpecializationDescription(dnd_class, specialization))
        self.changeClassTabChoice()
        self.wizard.character.dnd_class.specialization_name = specialization

    def changeClassTabChoice(self):
        """ Update the class choice widgets
        """
        dnd_class = self.page2_class_combo.currentText()
        specialization = self.page2_specialization_combo.currentText()
        list_choice = self.class_parser.getChoice(dnd_class)
        list_choice.extend(self.class_parser.getSpecializationChoice(dnd_class, specialization))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.page2_choice_list)):
            if (i == 0) or (i == len(self.page2_choice_list)-1):
                self.page2_choices_layout.removeItem(self.page2_choice_list[i])
            else:
                self.page2_choices_layout.removeWidget(self.page2_choice_list[i])
                self.page2_choice_list[i].deleteLater()

        self.page2_choice_list = []

        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.page2_choice_list.append(spacer)
        self.page2_choices_layout.addItem(spacer)
        j = 0
        for choice in list_choice:
            for i in range(choice[2]):
                j += 1
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.page2)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.page2_choices_layout.addWidget(label, j, 0)
                self.page2_choice_list.append(label)
                combo = QtGui.QComboBox(self.page2)
                combo.activated[str].connect(self.makeClassChoice)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                self.page2_choices_layout.addWidget(combo, j, 1)
                self.page2_choice_list.append(combo)

        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.page2_choice_list.append(spacer)
        self.page2_choices_layout.addItem(spacer)
        self.makeClassChoice(None)

    def makeClassChoice(self, useless):
        """ Update the list of choice in the character's background
        """
        choice = []
        for i in range(len(self.page2_choice_list)):
            if i%2 == 0 and i!=0:
                choice.append(str(self.page2_choice_list[i].currentText()))
                
        self.wizard.character.dnd_class.choice = choice

    # --------------- BACKGROUND FUNCTIONS ---------------------------------
        
    def changeBackground(self, background):
        """ action that will be done when the user change the background
        :param str background: New background
        """
        self.page3_ideal_combo.clear()
        self.page3_background_description.setText(
            self.background_parser.getDescription(background))
        perso_max = self.background_parser.getNumberPersonality(background)
        self.page3_personality_spinbox_1.setMaximum(perso_max)
        self.page3_personality_spinbox_2.setMaximum(perso_max)
        flaw_max = self.background_parser.getNumberFlaw(background)
        self.page3_flaw_spinbox.setMaximum(flaw_max)
        bond_max = self.background_parser.getNumberBond(background)
        self.page3_bond_spinbox.setMaximum(bond_max)
        for ideal in self.background_parser.getListIdeal(background):
            self.page3_ideal_combo.addItem(ideal)
        self.changeBackgroundChoice(background)
        self.wizard.character.background.setBackgroundName(background)
        money = self.background_parser.getMoney(background)
        self.wizard.character.money = money

        
    def changeIdealDescription(self, ideal):
        """ Update the text of the ideal
        :param str ideal: New Ideal
        """
        background = self.page3_background_combo.currentText()
        self.page3_ideal_description.setText(
            self.background_parser.getIdealDescription(background, ideal))
        self.wizard.character.background.setIdeal(ideal)

    def changePersonalityDescription(self, personality):
        """ Update the description text of the personality
        :param personality: Not used (present due to Qt)
        """
        background = self.page3_background_combo.currentText()
        perso1 = self.page3_personality_spinbox_1.value()
        perso2 = self.page3_personality_spinbox_2.value()
        if perso1 == perso2:
            self.page3_personality_description.setText(
                "Please choose two different personalities!")
            return
        self.wizard.character.background.setPersonality0(perso1)
        self.wizard.character.background.setPersonality1(perso2)
        perso1 = self.background_parser.getPersonalityDescription(
            background, perso1)
        perso2 = self.background_parser.getPersonalityDescription(
            background, perso2)
        text = "<p>" + perso1 + "</p> <p>" + perso2 + "</p>"
        self.page3_personality_description.setText(text)

    def changeBackgroundChoice(self, background):
        """ Update the background choice widgets
        :param str background: Background name
        """
        list_choice = self.background_parser.getChoice(background)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i in range(len(self.page3_choice_list)):
            # delete spacer
            if i%3 == 0:
                self.horizontalLayout_33.removeItem(self.page3_choice_list[i])
            # delete widget
            else:
                self.horizontalLayout_33.removeWidget(self.page3_choice_list[i])
                self.page3_choice_list[i].deleteLater()
                
        self.page3_choice_list = []
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.page3_choice_list.append(spacer)
        self.horizontalLayout_33.addItem(spacer)
        for choice in list_choice:
            for i in range(choice[2]):
                label = QtGui.QLabel(tools.choiceLabel(choice[0]), self.page3_choice_layout)
                label.setSizePolicy(sizePolicy)
                label.setAlignment(
                    QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_33.addWidget(label)
                self.page3_choice_list.append(label)
                combo = QtGui.QComboBox(self.page3_choice_layout)
                if choice[0] == 'language' and choice[1][0] == 'any':
                    choice = (choice[0], tools.getLanguages())
                for i in choice[1]:
                    combo.addItem(i)
                combo.activated[str].connect(self.makeBackgroundChoice)
                self.horizontalLayout_33.addWidget(combo)
                self.page3_choice_list.append(combo)
                spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                self.page3_choice_list.append(spacer)
                self.horizontalLayout_33.addItem(spacer)

        self.makeBackgroundChoice(None)

    def makeBackgroundChoice(self, useless):
        """ Update the list of choice in the character's background
        """
        choice = []
        for i in range(len(self.page3_choice_list)):
            if i%3 == 2:
                choice.append(str(self.page3_choice_list[i].currentText()))
                
        self.wizard.character.background.choice = choice
        
    def changeFlawDescription(self, flaw):
        """ Update the description of the flaw
        :param int flaw: value of the flaw
        """
        background = self.page3_background_combo.currentText()
        self.page3_flaw_description.setText(
            self.background_parser.getFlawDescription(background, flaw))
        self.wizard.character.background.setFlaw(flaw)

    def changeBondDescription(self, bond):
        """ Update the description of the bond
        :param int bond: value of the bond
        """
        background = self.page3_background_combo.currentText()
        self.page3_bond_description.setText(
            self.background_parser.getBondDescription(background, bond))
        self.wizard.character.background.setBond(bond)
        
    def fullRandomBackground(self):
        """ Choose randomly the background, personality, ideal, bond
        and flaw of the character
        """
        nber_background = len(self.background_parser.getListBackground())
        self.page3_background_combo.setCurrentIndex(
            tools.rollDice(1, nber_background) - 1)
        background = self.page3_background_combo.currentText()
        self.changeBackground(background)
        self.randomPersonality()

    def randomPersonality(self):
        """ Choose the personality of the character (bond, flaw, ideal,
        personality)
        """
        background = self.page3_background_combo.currentText()
        nber_perso = self.background_parser.getNumberPersonality(background)
        nber_flaw = self.background_parser.getNumberFlaw(background)
        nber_bond = self.background_parser.getNumberBond(background)
        nber_ideal = len(self.background_parser.getListIdeal(background))
        # bond
        self.page3_bond_spinbox.setValue(tools.rollDice(1, nber_bond))
        # flaw
        self.page3_flaw_spinbox.setValue(tools.rollDice(1, nber_flaw))
        # personality
        roll1 = tools.rollDice(1, nber_perso)
        self.page3_personality_spinbox_1.setValue(roll1)
        roll2 = tools.rollDice(1, nber_perso - 1)
        if roll2 >= roll1:
            roll2 += 1
        self.page3_personality_spinbox_2.setValue(roll2)
        # ideal
        self.page3_ideal_combo.setCurrentIndex(tools.rollDice(1, nber_ideal)-1)
        ideal = self.page3_ideal_combo.currentText()
        self.changeIdealDescription(ideal)

        # alignment
        align = self.background_parser.getIdealAlignement(background, ideal)
        if lower(align) == 'any':
            self.page3_alignment_combo.setCurrentIndex(tools.rollDice(1,9)-1)
        else:
            index_align = []
            for i in range(9):
                if lower(align) in lower(str(self.page3_alignment_combo.itemText(i))):
                    index_align.append(i)
            roll = tools.rollDice(1,len(index_align))-1
            self.page3_alignment_combo.setCurrentIndex(index_align[roll])
        self.wizard.character.background.setAlignment(
            self.page3_alignment_combo.currentText())
        
    # --------------------------- GUI ---------------------------------                    
        
        
    def setupNotes(self):
        self.page4 = QtGui.QWizardPage()
        self.page4.setObjectName(tools._fromUtf8("page4"))

        self.page4_main_layout = QtGui.QHBoxLayout(self.page4)
        self.page4_main_layout.setObjectName(tools._fromUtf8("page4_main_layout"))

        self.page4_groupbox = QtGui.QGroupBox("Notes", self.page4)
        self.page4_groupbox.setObjectName(tools._fromUtf8("Notes"))
        self.page4_main_layout.addWidget(self.page4_groupbox)
        
        self.page4_layout = QtGui.QHBoxLayout(self.page4_groupbox)
        self.page4_layout.setObjectName(tools._fromUtf8("page4_layout"))

        self.page4_notes = QtGui.QTextEdit(self.page4_groupbox)
        self.page4_notes.setObjectName(tools._fromUtf8("page4_notes"))
        
        self.page4_layout.addWidget(self.page4_notes)

        return self.page4
