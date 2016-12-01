from PyQt4 import QtGui, QtCore
from string import lower
from math import ceil

import gui.player.tools as tools
import core.spell as spell
import core.trait as trait
import core.race as race
import core.dnd_class as dnd_class
import core.character as character
from gui.player.setup_stat import setupStat
from gui.player.setup_spell import setupSpell
from gui.player.setup_trait import setupTrait

def abilityString(ability):
    mod = character.getModifier(ability)
    if mod > 0:
        mod = "+" + str(mod)
    mod = str(ability) + " (" + str(mod) + ")"
    return mod

class CharacterPlay(QtGui.QWidget):
    def setupUi(self, character):
        self.character = character
        self.setObjectName(tools._fromUtf8("MainWindow"))
        self.resize(1005, 719)
        self.setWindowTitle("Character Play")
        self.main_layout = QtGui.QHBoxLayout(self)
        self.main_tab = QtGui.QTabWidget(self)
        self.main_layout.addWidget(self.main_tab)

        self.race_parser = race.RaceParser()
        self.spell_parser = spell.SpellParser()
        self.trait_parser = trait.TraitParser()
        self.class_parser = dnd_class.DnDClassParser()
        setupStat(self)
        setupSpell(self)
        setupTrait(self)
        self.updateCharacter()
        self.updateStatList()

    def updateCharacter(self):
        # Strength
        ab = self.character.getStrength()
        text = abilityString(ab)
        self.tab0_str_value.setText(text)
        # Dexterity
        ab = self.character.getDexterity()
        text = abilityString(ab)
        self.tab0_dex_value.setText(text)
        # Constitution
        ab = self.character.getConstitution()
        text = abilityString(ab)
        self.tab0_con_value.setText(text)
        # Intelligence
        ab = self.character.getIntelligence()
        text = abilityString(ab)
        self.tab0_int_value.setText(text)
        # Wisdom
        ab = self.character.getWisdom()
        text = abilityString(ab)
        self.tab0_wis_value.setText(text)
        # Charisma
        ab = self.character.getCharisma()
        text = abilityString(ab)
        self.tab0_cha_value.setText(text)

        # Hit points
        hit_point = self.character.getHitPoint()
        hit_point = str(hit_point[0]) + "/" + str(hit_point[1])
        self.tab0_hit_points_value.setText(hit_point)

        # hit_dice
        temp = self.character.getHitDice()
        hit_dice = str(temp[0]) + "/" + str(temp[1])
        hit_dice += " d" + str(temp[2])
        self.tab0_hit_dice_value.setText(hit_dice)




    # --------------------------- STAT --------------------------------

    def updateStatList(self):
        if self.main_tab.currentIndex() != 0:
            return

        self.updateCharacter()
        self.tab0_spell_tree.clear()
        # cantrip
        root = self.tab1_tab0_known_tree.invisibleRootItem()
        if (root.childCount() > 0):
            cantrip = QtGui.QTreeWidgetItem(self.tab0_spell_tree, ["Cantrip"])
        for i in range(root.childCount()):
            item = root.child(i).clone()
            cantrip.addChild(item)
            
        # spell
        root = self.tab1_tab1_known_tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i).clone()
            self.tab0_spell_tree.invisibleRootItem().addChild(item)

        # trait
        self.tab0_trait_tree.clear()
        root = self.tab2_tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i).clone()
            self.tab0_trait_tree.invisibleRootItem().addChild(item)


    def longRest(self):
        new_hit_dice = int(ceil(character.getLevel(
            self.character.experience)/2.0))
        self.character.addHitDice(new_hit_dice)
        self.updateCharacter()

    def heal(self):
        dialog = HealDialog(self)
        hit, dice = dialog.setupUi()
        self.character.heal(hit, dice)
        self.updateCharacter()

    # --------------------------- SPELL -------------------------------

    def updateSpellDescription(self, value):
        """
        :param QTreeWidgetItem value: Spell name
        """
        self.character.dnd_class.hit_point -= 5
        if value is None or value.childCount() != 0:
            self.tab1_tab1_description.clear()
            return
        description = self.spell_parser.getDescription(value.text(0))
        self.tab1_tab1_description.setText(description)
        
        
    def updateCantripDescription(self, value):
        """
        :param QTreeWidgetItem value: Cantrip name
        """
        if value is None or value.childCount() != 0:
            self.tab1_tab0_description.clear()
            return
        description = self.spell_parser.getDescription(value.text(0))
        self.tab1_tab0_description.setText(description)
        
    
    def selectClassSpell(self, value):
        """ Update the list of spell and show only the spell of the given class
        :param str value: Class name
        """
        self.tab1_tab0_class_combo.setCurrentIndex(
            self.tab1_tab0_class_combo.findText(value))
        self.tab1_tab1_class_combo.setCurrentIndex(
            self.tab1_tab1_class_combo.findText(value))
        value = lower(str(value))
        if value == 'any':
            value = None
        self.tab1_tab0_list_tree.clear()
        self.tab1_tab1_list_tree.clear()
        self.tab1_tab1_lvl_1 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["1st Level"])
        self.tab1_tab1_lvl_2 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["2nd Level"])
        self.tab1_tab1_lvl_3 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["3rd Level"])
        self.tab1_tab1_lvl_4 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["4th Level"])
        self.tab1_tab1_lvl_5 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["5th Level"])
        self.tab1_tab1_lvl_6 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["6th Level"])
        self.tab1_tab1_lvl_7 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["7th Level"])
        self.tab1_tab1_lvl_8 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["8th Level"])
        self.tab1_tab1_lvl_9 = QtGui.QTreeWidgetItem(self.tab1_tab1_list_tree, ["9th Level"])
        for i in self.spell_parser.getListSpell(0, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab0_list_tree, i)
        for i in self.spell_parser.getListSpell(1, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_1, i)
        for i in self.spell_parser.getListSpell(2, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_2, i)
        for i in self.spell_parser.getListSpell(3, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_3, i)
        for i in self.spell_parser.getListSpell(4, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_4, i)
        for i in self.spell_parser.getListSpell(5, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_5, i)
        for i in self.spell_parser.getListSpell(6, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_6, i)
        for i in self.spell_parser.getListSpell(7, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_7, i)
        for i in self.spell_parser.getListSpell(8, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_8, i)
        for i in self.spell_parser.getListSpell(9, value):
            item = QtGui.QTreeWidgetItem(self.tab1_tab1_lvl_9, i)

    def _findLevelItemKnownSpell(self, level_text):
        """
        :param str level_text:
        :returns: QTreeWidgetItem
        """
        spell_tree = None
        if "1" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("1st Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["1st Level"])
            else:
                spell_tree = spell_tree[0]
        elif "2" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("2nd Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["2nd Level"])
            else:
                spell_tree = spell_tree[0]
        elif "3" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("3rd Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["3rd Level"])
            else:
                spell_tree = spell_tree[0]
        elif "4" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("4th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["4th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "5" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("5th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["5th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "6" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("6th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["6th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "7" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("7th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["7th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "8" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("8th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["8th Level"])
            else:
                spell_tree = spell_tree[0]
        elif "9" in level_text:
            spell_tree = self.tab1_tab1_known_tree.findItems("9th Level", QtCore.Qt.MatchFixedString, 0)
            if len(spell_tree) == 0:
                spell_tree = QtGui.QTreeWidgetItem(self.tab1_tab1_known_tree, ["9th Level"])
            else:
                spell_tree = spell_tree[0]
        return spell_tree

    def addSpell(self):
        item = self.tab1_tab1_list_tree.currentItem()
        level = self.tab1_tab1_known_tree.findItems("Level", QtCore.Qt.MatchContains, 0)
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
        item = self.tab1_tab1_known_tree.currentItem()
        parent = item.parent()
        parent.removeChild(item)
        if parent.childCount() == 0:
            index = parent.treeWidget().indexOfTopLevelItem(parent)
            parent.treeWidget().takeTopLevelItem(index)
    
    def addCantrip(self):
        item = self.tab1_tab0_list_tree.currentItem()
        matches = self.tab1_tab0_known_tree.findItems(item.text(0), QtCore.Qt.MatchFixedString, 0)
        if item.childCount() != 0 or len(matches) != 0:
            return
        cantrip = []
        for i in range(item.columnCount()):
            cantrip.append(item.text(i))
        QtGui.QTreeWidgetItem(self.tab1_tab0_known_tree, cantrip)
        
    def removeCantrip(self):
        item = self.tab1_tab0_known_tree.currentItem()
        index = item.treeWidget().indexOfTopLevelItem(item)
        item.treeWidget().takeTopLevelItem(index)

    # ---------------------------- TRAIT --------------------------

    def updateTraitDescription(self, value):
        if value is None:
            self.tab2_description.clear()
            return
        description = self.trait_parser.getDescription(value.text(0))
        self.tab2_description.setText(description)



class HealDialog(QtGui.QDialog):
    def setupUi(self):
        self.setWindowTitle("Heal")

        self.layout = QtGui.QVBoxLayout(self)
        self.l1 = QtGui.QLabel("Number of hit dice to use:", self)
        self.c1 = QtGui.QComboBox(self)
        for i in range(self.parent().character.getHitDice()[0] + 1):
            self.c1.addItem(str(i))
        self.form = QtGui.QFormLayout()
        self.layout.addLayout(self.form)
        self.form.addRow(self.l1, self.c1)

        self.l2 = QtGui.QLabel("Hit Point Healed:", self)
        self.le1 = QtGui.QLineEdit("", self)
        self.form.addRow(self.l2, self.le1)
        self.button = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        roll_button = QtGui.QPushButton("Roll", self)
        self.button.addButton(
            roll_button, QtGui.QDialogButtonBox.ActionRole)

        roll_button.clicked.connect(self.roll)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.layout.addWidget(self.button)

        self.exec_()
        if self.le1.text() == '':
            self.le1.setText('0')
        return int(self.le1.text()), int(self.c1.currentText())

    def roll(self):
        hit_dice = self.parent().character.getHitDice()
        roll_value = tools.rollDice(
            int(self.c1.currentText()), hit_dice[2])
        self.le1.setText(str(roll_value))
        self.accept()
