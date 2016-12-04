import xml.etree.ElementTree as ET
import string
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
        text = ET.tostringlist(child)
        # find end of <trait>
        i = 0
        test = True
        while i < len(text) and test:
            if '>' in text[i]:
                test = False
            i += 1
        # find start of </trait>
        test = True
        j = len(text) - 1
        while j > 0 and test:
            if '</' in text[j]:
                test = False
            j -= 1
            
        return string.join(text[i+1:j])

    def getMaxUse(self, name):
        child = self.getTrait(name)
        if child == None:
            return
        return child.get('max_use')
