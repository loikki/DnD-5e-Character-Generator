import xml.etree.ElementTree as ET
from os.path import join

import core.proficiency as pfy

class WeaponParser():
    def __init__(self):
        self.trait_file = join('data', 'dnd', 'weapon.xml')
        self.root = ET.parse(self.trait_file).getroot()

    def getWeapon(self, name):
        for child in self.root:
            if child.get('name') == name:
                return child

    def getDescription(self, name):
        child = self.getTrait(name)
        if child == None:
            return None
        return child.text
