import pickle
import os

from PyQt4 import QtGui, QtCore, QtNetwork
from string import lower
from math import ceil

import core.spell as spell
import core.trait as trait
import core.race as race
import core.dnd_class as dnd_class
import core.character as character
import core.equipment as equipment
import gui.tools as tools
import gui.player.dialogs as dialogs

from core.network.client import TCPClient
from gui.player.setup_stat import setupStat
from gui.player.setup_spell import setupSpell
from gui.player.setup_trait import setupTrait
from gui.player.setup_equipment import setupEquipment
            
def abilityString(ability):
    mod = character.getModifier(ability)
    if mod > 0:
        mod = "+" + str(mod)
    mod = str(ability) + " (" + str(mod) + ")"
    return mod

class CharacterPlay(QtGui.QWidget):
    def setupUi(self, character, dm=False):
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
        self.equipment_parser = equipment.EquipmentParser()

        setupStat(self)
        setupSpell(self)
        setupTrait(self)
        setupEquipment(self)
        self.updateCharacter()
        self.updateStatList()
        self.updateMoney()

        if not dm:
            ip_address, ok = QtGui.QInputDialog.getText(
                self, 'Connection to the DM', 
                'IP address of the DM:')

            if ok and ip_address != '':
                self.socket = TCPClient(self, ip_address)
        

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Save',
                    "Do you want to save your character?",
                    QtGui.QMessageBox.Yes | 
                    QtGui.QMessageBox.No |
                    QtGui.QMessageBox.Cancel,
                    QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            pickle.dump(self.character, open(os.path.join(
                "data", "saved", "player",
                self.character.name + ".p"), 'wb'))

        
        if reply == QtGui.QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()
        
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
        dialog = dialogs.HealDialog(self)
        hit, dice = dialog.setupUi()
        self.character.heal(hit, dice)
        if hasattr(self, 'socket'):
            self.socket.sendDataToDM("heal", hit)
        self.updateCharacter()

    def takeDamage(self, value):
        self.character.dnd_class.hit_point -= value
        QtGui.QMessageBox.information(self, "Damage",
            "You just received " + str(value) + " damage!")
        self.updateCharacter()
        if self.character.dnd_class.hit_point < 1:
            dialog = dialogs.DeathDialog(self)
            dead, healed = dialog.setupUi()
            if dead:
                QtGui.QMessageBox.information(
                    self, "Game Over", "You are dead!")
            else:
                QtGui.QMessageBox.information(self,
                    "Not Game Over", "Come back, you are still alive!")
                if healed:
                    self.character.dnd_class.hit_point = 1

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


    # ------------------------- EQUIPMENT -------------------------

    def updateEquipmentDescription(self, value):
        if value is None:
            self.tab3_description.clear()
            return
        description = self.equipment_parser.getDescription(value.text(0))
        self.tab3_description.setText(description)

    def addEquipment(self):
        index = self.tab3_tabwidget.currentIndex()
        if index == 0: # weapon
            tree = self.tab3_tab0_owned_tree
            item = self.tab3_tab0_list_tree.currentItem()
        elif index == 1: # armor
            tree = self.tab3_tab1_owned_tree
            item = self.tab3_tab1_list_tree.currentItem()
        elif index == 2: # gear
            tree = self.tab3_tab2_owned_tree
            item = self.tab3_tab2_list_tree.currentItem()

        if item == None:
            return
        
        root = tree.invisibleRootItem()
        temp_item = item.clone()
        root.addChild(temp_item)
        self.updateCarryCapacity()

    def removeEquipment(self):
        index = self.tab3_tabwidget.currentIndex()
        if index == 0: # weapon
            tree = self.tab3_tab0_owned_tree
        elif index == 1: # armor
            tree = self.tab3_tab1_owned_tree
        elif index == 2: # gear
            tree = self.tab3_tab2_owned_tree
        
        root = tree.invisibleRootItem()
        item = tree.currentItem()
        root.removeChild(item)
        self.updateCarryCapacity()
        
    def buyEquipment(self):
        index = self.tab3_tabwidget.currentIndex()
        if index == 0: # weapon
            item = self.tab3_tab0_list_tree.currentItem()
        elif index == 1: # armor
            item = self.tab3_tab1_list_tree.currentItem()
        elif index == 2: # gear
            item = self.tab3_tab2_list_tree.currentItem()
        default = tools.getMoneyFromString(str(item.text(1)))
        dialog = dialogs.MoneyDialog(self)
        ok, cost = dialog.setupUi("Buy Equipment", default)
        cost = tools.totalMoney(cost)
        if cost > self.character.money:
            ok = False
            QtGui.QMessageBox.information(
                self, "You are POOR!", "You do not have enough money!")
        
        if ok:
            self.character.money -= cost
            self.addEquipment()
            self.updateMoney()

    def sellEquipment(self):
        index = self.tab3_tabwidget.currentIndex()
        if index == 0: # weapon
            item = self.tab3_tab0_owned_tree.currentItem()
        elif index == 1: # armor
            item = self.tab3_tab1_owned_tree.currentItem()
        elif index == 2: # gear
            item = self.tab3_tab2_owned_tree.currentItem()
        default = tools.getMoneyFromString(str(item.text(1)))
        dialog = dialogs.MoneyDialog(self)
        ok, cost = dialog.setupUi("Sell Equipment", default)
        cost = tools.totalMoney(cost)
        if ok:
            self.character.money += cost
            self.removeEquipment()
            self.updateMoney()


    def updateMoney(self):
        money = tools.generateMoneyString(self.character.money)
        self.tab3_gold_label.setText(money)
        if hasattr(self, 'socket'):
            self.socket.sendDataToDM("money", self.character.money)

    def earnMoney(self):
        dialog = dialogs.MoneyDialog(self)
        ok, cost = dialog.setupUi("Earn/Loose Money", 0)
        cost = tools.totalMoney(cost)
        if ok:
            self.character.money += cost
            self.updateMoney()

    def updateCarryCapacity(self):
        weight = 0
        root = self.tab3_tab0_owned_tree.invisibleRootItem()
        # weapon
        for i in range(root.childCount()):
            text = str(root.child(i).text(3)).split(" ")[0]
            if not "-" in text:
                weight += float(text)

        # armor
        root = self.tab3_tab1_owned_tree.invisibleRootItem()
        for i in range(root.childCount()):
            text = str(root.child(i).text(5)).split(" ")[0]
            if not "-" in text:
                weight += float(text)

        # gear
        root = self.tab3_tab2_owned_tree.invisibleRootItem()
        for i in range(root.childCount()):
            text = str(root.child(i).text(2)).split(" ")[0]
            if not "-" in text:
                weight += float(text)

        text = " "*10 + "Carry: " + str(weight) + "/"
        text += str(self.character.getCarryingCapacity())
        text += " lb."
        self.tab3_carry_label.setText(text)
        if weight > self.character.getCarryingCapacity():
            self.tab3_carry_label.setStyleSheet(
                "QLabel { color : red; }")
        else:
            self.tab3_carry_label.setStyleSheet(
                "QLabel { color : black; }")

