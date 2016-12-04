from PyQt4 import QtGui, QtCore
import random
from string import replace, lower
import math


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



def rollDice(number_dice, type_dice):
    """ roll (number_dice)d(type_dice)
    :param int number_dice: Number of dice to roll
    :param int type_dice: Type of dice (d4, d6, ...)
    :returns: Value
    """
    value = 0
    for i in range(number_dice):
        value += random.randint(1,type_dice)
    return value

def rollAbility():
    """ Roll 4d6 and remove the lowest one.
    :return: Value of the rolls
    """
    rolls = [rollDice(1,6), rollDice(1,6), rollDice(1,6), rollDice(1,6)]
    min_ind = rolls.index(min(rolls))
    value = 0
    for i in range(len(rolls)):
        if i != min_ind:
            value += rolls[i]
    return value

def choiceLabel(title):
    """ Make the title nice
    :param str title: String to process
    :returns: str with a nice presentation
    """
    title = title.title()
    return replace(title, '_', ' ')

def getLanguages(allow_exotic=False):
    """ Return the list of available languages
    :param bool allow_exotic: Add the exotic languages to the list
    :returns: [str] List of all the available languages
    """
    languages = ['Common', 'Dwarvish', 'Elvish', 'Giant', 'Gnomish',
                 'Goblin', 'Halfling', 'Orc']
    if allow_exotic:
        languages.extend(['Abyssal', 'Celestial', 'Draconic', 'Deep Speech',
                          'Infernal', 'Primordial', 'Sylvan', 'Undercommon'])
    return languages


def createObjectProficiencyLabel(self, list_prof, enum_prof, current_index=0, parent='loader'):
    """
    :param list list_prof: Proficiency list from the class Proficiency
    :param Enum enum_prof: Enum proficiency class
    """
    if parent == 'loader':
        grid = self.gridLayout_16
        object_layout = self.object_proficiency_layout
        list_object = self.list_object
    elif parent == 'play':
        grid = self.object_gridLayout
        object_layout = self.tab0_object_layout
        list_object = self.tab0_list_object
        
    for i in range(len(list_prof)):
        if list_prof[i]:
            label = QtGui.QLabel(
                choiceLabel(enum_prof(i).name),
                object_layout)
            label.setAlignment(QtCore.Qt.AlignCenter)
            grid.addWidget(
                label, int(current_index/2), current_index%2)
            list_object.append(label)
            current_index += 1
    return current_index

