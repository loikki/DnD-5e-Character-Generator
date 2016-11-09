import xml.etree.ElementTree as ET

class DnDClassParser:
    def __init__(self):
        self.class_file = 'data/dnd/class.xml'
        self.root = ET.parse(self.class_file).getroot()

    def getClass(self, dnd_class):
        """ give the element structure of the required class
        :param str dnd_class: Name of the class
        :returns: ElementTree
        """
        for child in self.root:
            if child.get('name') == dnd_class:
                return child

    def getListClass(self):
        """ Gives a list of class
        :returns: List of class name
        """        
        list_class = []
        for child in self.root:
            list_class.append(child.get('name'))
        return list_class

    def getDescription(self, dnd_class):
        """ Gives the description of the requested class
        :param str class: Class name
        :returns: String containing the full description
        """
        child = self.getClass(dnd_class)
        if child == None:
            return None
        description = ET.tostring(child.find('description'))
        ind_open = description.index("<description>")
        ind_close = description.index("</description>")
        description = description[ind_open+13:ind_close]
        return description

    def getChoice(self, dnd_class):
        """ Gives the possible choice to make for a class
        :param str dnd_class: Class name
        :returns: [(choice's tag, choice's list, number of choice), ...]
        """
        child = self.getClass(dnd_class)
        list_choice = []
        for choice in child.find('choice'):
            value = (choice.tag, [], int(choice.get('quantity')))
            for key in choice.findall('key'):
                value[1].append(key.get('name'))
            list_choice.append(value)
        return list_choice


    def getListSpecialization(self, dnd_class):
        """ Gives a list of specialization possible for a given class
        :param str dnd_class: Class name
        :returns: [str] List of the specialization
        """
        list_specialization = []
        child = self.getClass(dnd_class)
        for specialization in child.findall('specialization'):
            list_specialization.append(specialization.get('name'))
        return list_specialization

    def getSpecialization(self, dnd_class, specialization):
        """ Gives the element structure of the required specialization
        :param str dnd_class: Class name
        :param str specialization: Specialization name
        :returns: ElementTree containing the specialization
        """
        child = self.getClass(dnd_class)
        for class_child in child.findall('specialization'):
            if class_child.get('name') == specialization:
                return class_child

    def getSpecializationDescription(self, dnd_class, specialization):
        """ Gives the description of the specialization
        :param str dnd_class: Class name
        :param str specialization: Subrace name
        :returns: String containing the full description
        """
        child = self.getSpecialization(dnd_class, specialization)
        description = ET.tostring(child.find('description'))
        ind_open = description.index("<description>")
        ind_close = description.index("</description>")
        description = description[ind_open+13:ind_close]
        return description

    def getSpecializationChoice(self, dnd_class, specialization):
        """ Gives the possible choice to make for a specialization
        :param str dnd_class: Class name
        :param str specialization: Specialization name
        :returns: [(choice's tag, choice's list, number of choice), ...]
        """
        child = self.getSpecialization(dnd_class, specialization)
        list_choice = []
        child_test = child.find('choice')
        if child_test is None:
            return []
        for choice in child_test:
            value = (choice.tag, [], int(choice.get('quantity')))
            for key in choice.findall('key'):
                value[1].append(key.get('name'))
            list_choice.append(value)
        return list_choice


class DnDClass:
    def __init__(self):
        self.class_name = None
        self.specialization_name = None

    def write(self):
        print "Class: ", self.class_name
        print "Specialization: ", self.specialization_name
