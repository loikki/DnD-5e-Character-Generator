import xml.etree.ElementTree as ET
from os.path import join

class SpellParser():
    def __init__(self):
        self.parser_file = join('data', 'dnd', 'spell.xml')
        self.root = ET.parse(self.parser_file).getroot()

    def getSpell(self, name):
        for child in self.root:
            if child.get('name') == name:
                return child

    def getListSpell(self, level, dndclass):
        """ Get all the list of the required level
        level 0 = cantrip
        :param int level: Level of the spell (None for all level)
        :param str dndclass: Class name
        :returns: [(name, casting_time, range, component, duration)]
        """
        list_spell = []
        for child in self.root:
            if level == 0 and child.tag == "cantrip":
                list_spell.append((
                    child.get('name'), child.get('casting_time'),
                    child.get('range'), child.get('component'),
                    child.get('duration'), child.get('type')))
            if (child.tag == "spell" and (int(child.get('level')) == level or level is None)
                and (dndclass is None or dndclass in child.get('class'))):
                list_spell.append((
                    child.get('name'), child.get('casting_time'),
                    child.get('range'), child.get('component'),
                    child.get('duration'), child.get('type')))

        return list_spell


    def getDescription(self, name):
        child = self.getSpell(name)
        if child == None:
            return None
        description = "<p><b><u>" + str(name) + "</u></b></p>\n"

        if child.tag == 'spell':
            description += "<p><b> Level </b>" + str(child.get('level')) + " "
        else:
            description += "<p><b> Cantrip </b> "
        description += child.get('type') + "</p>" + "\n"

        description += "<p><b> Casting Time </b>" + str(child.get('casting_time')) + "</p>\n"
        description += "<p><b> Range </b>" + str(child.get('range')) + "</p>\n"
        description += "<p><b> Components </b>" + str(child.get('component')) + "</p>\n"
        description += "<p><b> Duration </b>" + str(child.get('duration')) + "</p>\n"

        temp = ET.tostring(child.find('description'))
        ind_open = temp.index("<description>")
        ind_close = temp.index("</description>")
        description += temp[ind_open+13:ind_close]

        return description
