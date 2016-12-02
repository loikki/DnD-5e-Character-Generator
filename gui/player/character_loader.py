from PyQt4 import QtCore, QtGui
import os
import pickle

import core.proficiency as proficiency

import gui.player.tools as tools
from gui.player.setup_character_choice import setupCharacterChoice
from gui.player.character_generator import CharacterGenerator
from gui.player.character_play import CharacterPlay


class CharacterLoader(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(tools._fromUtf8("MainWindow"))
        MainWindow.resize(1005, 719)
        MainWindow.setWindowTitle("Character's Loader")
        self.main_window = MainWindow

        # Create main tab
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(tools._fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.loaded_characters = []
        
        setupCharacterChoice(self)

    def newCharacter(self):
        self.generator = CharacterGenerator()
        self.generator.setupUi(self)
        
    def loadCharacter(self):
        character = self.character_choice.currentItem().text()
        for c in self.list_character:
            if character == c.name:
                character = c
                break
        char_play = CharacterPlay()
        char_play.setupUi(character)
        char_play.show()
        self.loaded_characters.append(char_play)

    def deleteCharacter(self):
        character = str(self.character_choice.currentItem().text())
        question = "Do you really want to delete " + character + "?"
        response = QtGui.QMessageBox.question(
            self.centralwidget, 'Message',
            question, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if response == QtGui.QMessageBox.Yes:
            os.remove(os.path.join("data", "saved", "player", character + ".p"))
        self.loadListCharacters()
        
    # --------------- Character Choice ------------------------------------

    def loadListCharacters(self):
        self.list_character = []
        character_directory = os.path.join("data", "saved", "player", "")
        for character_file in os.listdir(character_directory):
            self.list_character.append(pickle.load(
                open(character_directory + character_file, 'rb')))
        self.character_choice.clear()
        for character in self.list_character:
            self.character_choice.addItem(character.name)

    def printSummary(self):
        character = self.character_choice.currentItem()
        if character is None:
            return
        character = character.text()
        
        for c in self.list_character:
            if character == c.name:
                character = c
                break

        self.raceLineEdit.setText(character.race.subrace_name)
        self.classLineEdit.setText(character.dnd_class.class_name)
        self.specializationLineEdit.setText(
            character.dnd_class.specialization_name)
        self.backgroundLineEdit.setText(
            character.background.background_name)
        self.experienceLevelLineEdit.setText(
            str(character.experience))
        if c.image is not None:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(c.image)
            max_size = 150
            if pixmap.height() > pixmap.width():
                pixmap = pixmap.scaledToHeight(max_size)
            else:
                pixmap = pixmap.scaledToWidth(max_size)
            self.img.setPixmap(pixmap)
        else:
            self.img.clear()
        self.str_value.setText(str(character.getStrength()))
        self.dex_value.setText(str(character.getDexterity()))
        self.con_value.setText(str(character.getConstitution()))
        self.int_value.setText(str(character.getIntelligence()))
        self.wis_value.setText(str(character.getWisdom()))
        self.cha_value.setText(str(character.getCharisma()))
        character.background.getProficiency(None)
        self.loadProficiency(character)


    def loadProficiency(self, character):
        for i in range(len(self.list_skill)):
            self.gridLayout_15.removeWidget(self.list_skill[i])
            self.list_skill[i].deleteLater()

        self.list_skill = []
        # skills
        prof, diff = character.getProficiency()
        skills = prof.skills
        j = 0
        for i in range(len(skills)):
            if skills[i]:
                label = QtGui.QLabel(
                    tools.choiceLabel(proficiency.SkillProficiency(i).name),
                    self.skill_layout)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.gridLayout_15.addWidget(label, int(j/2), j%2)
                self.list_skill.append(label)
                j += 1

        # Saving
        saving = prof.saving
        for i in range(len(self.list_saving)):
            self.hLayout_saving.removeWidget(self.list_saving[i])
            self.list_saving[i].deleteLater()
        self.list_saving = []

        for i in range(len(saving)):
            if saving[i]:
                label = QtGui.QLabel(
                    tools.choiceLabel(proficiency.Ability(i).name),
                    self.saving_layout)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.hLayout_saving.addWidget(label)
                self.list_saving.append(label)

        # Object
        for i in range(len(self.list_object)):
            self.gridLayout_16.removeWidget(self.list_object[i])
            self.list_object[i].deleteLater()
        self.list_object = []
        weapon = prof.weapons
        j = tools.createObjectProficiencyLabel(
            self, weapon, proficiency.WeaponProficiency)
        tool = prof.tools
        j = tools.createObjectProficiencyLabel(
            self, tool, proficiency.ToolProficiency, j)
        armor = prof.armors
        j = tools.createObjectProficiencyLabel(
            self, armor, proficiency.ArmorProficiency, j)   

        # Languages
        for i in range(len(self.list_lang)):
            self.lang_gridLayout.removeWidget(self.list_lang[i])
            self.list_lang[i].deleteLater()

        self.list_lang = []
        
        lang = prof.languages
        j = 0
        for i in range(len(lang)):
            if skills[i]:
                label = QtGui.QLabel(
                    tools.choiceLabel(proficiency.LanguageProficiency(i).name),
                    self.lang_proficiency_layout)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.lang_gridLayout.addWidget(label, int(j/2), j%2)
                self.list_lang.append(label)
                j += 1
