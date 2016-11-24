import xml.etree.ElementTree as ET
from os.path import join

import core.proficiency as pfy

class TraitParser():
    def __init__(self):
        self.trait_file = join('data', 'dnd', 'trait.xml')
        self.root = ET.parse(self.trait_file).getroot()

    def getTrait(self, name):
        for child in self.root:
            if child.get('name') == name:
                return child

    def getDescription(self, name):
        child = self.getTrait(name)
        if child == None:
            return None
        return child.text

    def getMaxUse(self, name):
        child = self.getTrait(name)
        if child == None:
            return
        return child.get('max_use')
