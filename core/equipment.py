import xml.etree.ElementTree as ET
from os.path import join

class EquipmentParser():
    def __init__(self):
        self.parser_file = join('data', 'dnd', 'equipment.xml')
        self.root = ET.parse(self.parser_file).getroot()

    def getEquipment(self, name):
        for child in self.root:
            if child.get('name') == name:
                return child

    def getListWeapon(self):
        """ Get the list of weapons
        :return: list to parse for the QTreeWidget
        """
        list_equipment = []
        for child in self.root:
            if child.tag == 'weapon':
                list_equipment.append((
                    child.get('name'), child.get('cost'),
                    child.get('damage'), child.get('weight'),
                    child.get('properties'), child.get('type')))
        return list_equipment

    def getListArmor(self):
        """ Get the list of armor
        :return: list to parse for the QTreeWidget
        """
        list_equipment = []
        for child in self.root:
            if child.tag == 'armor':
                list_equipment.append((
                    child.get('name'), child.get('cost'),
                    child.get('ac'), child.get('strength'),
                    child.get('stealth'), child.get('weight'),
                    child.get('type')))
        return list_equipment

    def getListGear(self):
        """ Get the list of gear
        :return: list to parse for the QTreeWidget
        """
        list_equipment = []
        for child in self.root:
            if child.tag == 'gear':
                list_equipment.append((
                    child.get('name'), child.get('cost'),
                    child.get('weight'), child.get('quantity')))
        return list_equipment

    def getListPackage(self):
        print "TODO"

    def getDescription(self, name):
        child = self.getSpell(name)
        if child == None:
            return None
        description = "<p><b><u>" + str(name) + "</u></b></p>\n"

        temp = ET.tostring(child.find('description'))
        ind_open = temp.index("<description>")
        ind_close = temp.index("</description>")
        description += temp[ind_open+13:ind_close]

        return description
