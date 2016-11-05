import xml.etree.ElementTree as ET

class BackgroundParser():
    def __init__(self):
        self.background_file = 'data/dnd/background.xml'
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
                return ideal.text

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
        self.skill = None
        self.language_choosen = None
        self.equipment = []
        self.money = None
        self.personality = []
        self.ideal = []
        self.bond = []
        self.flaw = []
