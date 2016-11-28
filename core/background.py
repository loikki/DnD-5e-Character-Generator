import xml.etree.ElementTree as ET
from string import lower
from os.path import join

import core.proficiency as pfy

class BackgroundParser():
    def __init__(self):
        self.background_file = join('data', 'dnd', 'background.xml')
        self.root = ET.parse(self.background_file).getroot()

    def getBackground(self, name):
        for child in self.root:
            if child.get('name') == name:
                return child

    def getListBackground(self):
        list_background = []
        for child in self.root:
            list_background.append(child.get('name'))
        return list_background

    def getDescription(self, name):
        child = self.getBackground(name)
        if child == None:
            return None
        description = ET.tostring(child.find('description'))
        ind_open = description.index("<description>")
        ind_close = description.index("</description>")
        description = description[ind_open+13:ind_close]
        return description

    def getListIdeal(self, background):
        child = self.getBackground(background)
        if child == None:
            return None
        list_ideal = []
        ideals = child.find('ideal')
        for ideal in ideals.findall('description'):
            list_ideal.append(ideal.get('name'))
        return list_ideal

    def getIdealDescription(self, background, ideal_name):
        child = self.getBackground(background)
        for ideal in child.find('ideal'):
            if ideal.get('name') == ideal_name:
                description = '<p align="center">' + ideal.text
                description += "(" + ideal.get('alignment') + ")</p>"
                return description

    def getIdealAlignement(self, background, ideal_name):
        child = self.getBackground(background)
        for ideal in child.find('ideal'):
            if ideal.get('name') == ideal_name:
                return ideal.get('alignment')

    def getFlawDescription(self, background, value):
        child = self.getBackground(background)
        for flaw in child.find('flaw'):
            if int(flaw.get('value')) == value:
                return flaw.text

    def getNumberFlaw(self, background):
        value = 0
        child = self.getBackground(background)
        for flaw in child.find('flaw'):
            value += 1
        return value

            
    def getBondDescription(self, background, value):
        child = self.getBackground(background)
        for bond in child.find('bond'):
            if int(bond.get('value')) == value:
                return bond.text

    def getNumberBond(self, background):
        value = 0
        child = self.getBackground(background)
        for bond in child.find('bond'):
            value += 1
        return value

    def getPersonalityDescription(self, background, value):
        child = self.getBackground(background)
        for personality in child.find('personality'):
            if int(personality.get('value')) == value:
                return personality.text

    def getNumberPersonality(self, background):
        value = 0
        child = self.getBackground(background)
        for personality in child.find('personality'):
            value += 1
        return value

    def getChoice(self, background):
        """ returns [(type, choice, number of choice)]
        """
        child = self.getBackground(background)
        list_choice = []
        for choice in child.find('choice'):
            value = (choice.tag, [], int(choice.get('quantity')))
            for key in choice.findall('key'):
                value[1].append(key.get('name'))
            list_choice.append(value)
        return list_choice
        

class Background():
    def __init__(self):
        self.background_name = None
        self.flaw = None
        # list containing the index of the choice
        self.choice = []
        # two values
        self.personality = [None, None]
        self.ideal = None
        self.bond = None
        self.alignment = None

    def setBackgroundName(self, name):
        self.background_name = name

    def setFlaw(self, flaw):
        self.flaw = flaw

    def setIdeal(self, ideal):
        self.ideal = ideal

    def setPersonality1(self, pers):
        self.personality[1] = pers

    def setPersonality0(self, pers):
        self.personality[0] = pers

    def setBond(self, bond):
        self.bond = bond

    def setAlignment(self, alignment):
        self.alignment = alignment
        
    def write(self):
        print "Background: ", self.background_name
        print "Flaw: ", self.flaw
        print "Personality: ", self.personality
        print "Ideal: ", self.ideal
        print "Bond: ", self.bond
        print "Alignment: ", self.alignment
        print "Choice: ", self.choice

        print "Proficiency: "
        self.getProficiency(None)[0].write()

    def getProficiency(self, parser=None, proficiency=None):
        """
        :param BackgroundParser parser: If none, create one
        """
        if proficiency is None:
            proficiency = pfy.Proficiency()
        if parser is None:
            parser = BackgroundParser()

        background = parser.getBackground(self.background_name)
        prof = background.find('proficiency')
        proficiency, diff = pfy.getLocalProficiency(prof, proficiency)

        if len(self.choice) > 0:
            choice = parser.getChoice(self.background_name)
            i = 0
            for value in choice:
                proficiency, temp = pfy.getChoiceProficiency(
                    proficiency, value, self.choice[i:i+value[2]])
                if not temp:
                    diff = temp
                i += value[2]

        return proficiency, diff
