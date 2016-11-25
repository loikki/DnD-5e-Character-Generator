
self.spell_parser = spell.SpellParser()
self.trait_parser = trait.TraitParser()

setupSpell(self)
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

