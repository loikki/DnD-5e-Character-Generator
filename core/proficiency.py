from enum import Enum
from string import lower, replace

def toProficiencyName(string):
    string = lower(string)
    return replace(string, ' ', '_')

def getLocalProficiency(parser, proficiency):
    """
    :param ElementTreeObject parser: Parser
    :param Proficiency proficiency: object where to add proficiencies
    :returns: Completed ObjectProficiency, different
    """
    diff = True
    for i in parser.findall("saving_throw"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addSavingProficiency(name)
        if not temp:
            diff = False
    for i in parser.findall("skill"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addSkillProficiency(name)
        if not temp:
            diff = False
    for i in parser.findall("weapon"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addWeaponProficiency(name)
        if not temp:
            diff = False
    for i in parser.findall("armor"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addArmorProficiency(name)
        if not temp:
            diff = False
    for i in parser.findall("tool"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addToolProficiency(name)
        if not temp:
            diff = False
    for i in parser.findall("language"):
        name = toProficiencyName(i.get('name'))
        temp = proficiency.addLanguageProficiency(name)
        if not temp:
            diff = False

    return proficiency, diff

def getChoiceProficiency(proficiency, value, choice):
    """
    :param Proficiency proficiency: object where to add proficiencies
    :param tuple value: (tag, choice, number of choice)
    :param [str] choice: list of choosen values (size given by number of choice)
    :returns: proficiencies, different
    """
    diff = True
    if value[2] != len(choice):
        raise Exception("Number of choice not respected")
    for i in choice:
        if value[0] == 'saving_throw':
            temp = proficiency.addSavingProficiency(lower(str(i)))
            if not temp:
                diff = False
        if value[0] == 'language':
            temp = proficiency.addLanguageProficiency(lower(str(i)))
            if not temp:
                diff = False
        elif value[0] == 'skill':
            temp = proficiency.addSkillProficiency(lower(str(i)))
            if not temp:
                diff = False
        elif value[0] == 'weapon':
            temp = proficiency.addWeaponProficiency(lower(str(i)))
            if not temp:
                diff = False
        elif value[0] == 'armor':
            temp = proficiency.addArmorProficiency(lower(str(i)))
            if not temp:
                diff = False
        elif value[0] == 'tool':
            temp = proficiency.addToolProficiency(lower(str(i)))
            if not temp:
                diff = False
    return proficiency, diff

class Ability(Enum):
    strength = 0
    dexterity = 1
    constitution = 2
    intelligence = 3
    wisdom = 4
    charisma = 5


class SkillProficiency(Enum):
    acrobatics = 0
    animal_handling = 1
    arcana = 2
    athletics = 3
    deception = 4
    history = 5
    insight = 6
    intimidation = 7
    investigation = 8
    medicine = 9
    nature = 10
    perception = 11
    performance = 12
    persuasion = 13
    religion = 14
    sleight_of_hand = 15
    stealth = 16
    survival = 17

class WeaponProficiency(Enum):
    # simple melee
    club = 0
    dagger = 1
    greatclub = 2
    handaxe = 3
    javelin = 4
    light_hammer = 5
    mace = 6
    quarterstaff = 7
    sickle = 8
    spear = 9
    unarmed_strike = 10
    # simple ranged
    light_crossbow = 11
    dart = 12
    shortbow = 13
    sling = 14
    # martial melee
    battleaxe = 15
    flail = 16
    glaive = 17
    greataxe = 18
    greatsword = 19
    halberd = 20
    lance = 21
    longsword = 22
    maul = 23
    morningstar = 24
    pike = 25
    rapier = 26
    scimitar = 27
    shortsword = 28
    trident = 29
    war_pick = 30
    warhammer = 31
    whip = 32
    # martial ranged
    blowgun = 33
    hand_crossbow = 34
    heavy_crossbow = 35
    longbow = 36
    net = 37

class ArmorProficiency(Enum):
    light = 0
    medium = 1
    heavy = 2

class ToolProficiency(Enum):
    # Artisan
    alchemist = 0
    brewer = 1
    calligrapher = 2
    carpenter = 3
    cartographer = 4
    cobbler = 5
    cook = 6
    glassblower = 7
    jeweler = 8
    leatherworker = 9
    mason = 10
    painter = 11
    potter = 12
    smith = 13
    tinker = 14
    weaver = 15
    woodcarver = 16
    # Disguise
    disguise = 17
    # Forgery
    forgery = 18
    # Gaming
    dice = 19
    dragonchess = 20
    playing_card = 21
    three_dragon_ante = 22
    # Herbalism
    herbalism = 23
    # Music
    bagpipes = 24
    drum = 25
    dulcimer = 26
    flute = 27
    lute = 28
    lyre = 29
    horn = 30
    pan_flute = 31
    shawn = 32
    viol = 33
    # Navigator
    navigator = 34
    # Poisoner
    poisoner = 35
    # Thieves
    thieves = 36
    # Vehicles
    land_vehicles = 37
    water_vehicles = 38

class LanguageProficiency(Enum):
    common = 0
    dwarvish = 1
    elvish = 2
    giant = 3
    gnomish = 4
    goblin = 5
    halfling = 6
    orc = 7
    abyssal = 8
    celestial = 9
    draconic = 10
    deep_speech = 11
    infernal = 12
    primordial = 13
    sylvan = 14
    undercommon = 15

class Proficiency():
    def __init__(self):
        self.saving = [False]*6
        self.skills = [False]*18
        self.weapons = [False]*38
        self.tools = [False]*39
        self.armors = [False]*3
        self.languages = [False]*16

    def addLanguageProficiency(self, prof):
        prof = LanguageProficiency[prof]
        diff = True
        if self.languages[prof.value]:
            diff = False
        self.languages[prof.value] = True
        return diff

    def addSavingProficiency(self, prof):
        prof = Ability[prof]
        diff = True
        if self.saving[prof.value]:
            diff = False
        self.saving[prof.value] = True
        return diff
    
    def addSkillProficiency(self, prof):
        prof = SkillProficiency[prof]
        diff = True
        if self.skills[prof.value]:
            diff = False
        self.skills[prof.value] = True
        return diff
        
    def addWeaponProficiency(self, prof):
        diff = True
        if prof == "simple":
            for i in self.weapons[0:15]:
                if i:
                    diff = False
            self.weapons[0:15] = True
        elif prof == "martial":
            for i in self.weapons[0:15]:
                if i:
                    diff = False
            self.weapons[15:0] = True
        else:
            prof = WeaponProficiency[prof]
            if self.weapons[prof.value]:
                diff = False
            self.weapons[prof.value] = True
        return diff

    def addArmorProficiency(self, prof):
        prof = ArmorProficiency[prof]
        diff = True
        if self.armor[prof.value]:
            diff = False
        self.armors[prof.value] = True
        return diff

    def addToolProficiency(self, prof):
        prof = ToolProficiency[prof]
        diff = True
        if self.tools[prof.value]:
            diff = False
        self.tools[prof.value] = True
        return diff

    def write(self):
        print "Saving Throws:\n"
        for i in range(len(self.saving)):
            if self.saving[i]:
                print Ability(i).name.title()
        print "Skills:\n"
        for i in range(len(self.skills)):
            if self.skills[i]:
                print SkillProficiency(i).name.title()
        print "Weapons:\n"
        for i in range(len(self.weapons)):
            if self.weapons[i]:
                print WeaponProficiency(i).name.title()
        print "Armor:\n"
        for i in range(len(self.armors)):
            if self.armors[i]:
                print ArmorProficiency(i).name.title()
        print "Tools:\n"
        for i in range(len(self.tools)):
            if self.tools[i]:
                print ToolProficiency(i).name.title()
        print "Languages:\n"
        for i in range(len(self.languages)):
            if self.languages[i]:
                print LanguageProficiency(i).name.title()

    def getProficiency(self):
        prof = {}
        prof["Saving Throws"] = []
        for i in range(len(self.saving)):
            if self.saving[i]:
                prof["Saving Throws"].append(
                    Ability(i).name.title())
        prof["Skills"] = []
        for i in range(len(self.skills)):
            if self.skills[i]:
                prof["Skills"].append(
                    SkillProficiency(i).name.title())
        prof["Weapons"] = []
        for i in range(len(self.weapons)):
            if self.weapons[i]:
                prof["Weapons"].append(
                    WeaponProficiency(i).name.title())
        prof["Armors"] = []
        for i in range(len(self.armors)):
            if self.armors[i]:
                prof["Armors"].append(
                    ArmorProficiency(i).name.title())
        prof["Tools"] = []
        for i in range(len(self.tools)):
            if self.tools[i]:
                prof["Tools"].append(
                    ToolProficiency(i).name.title())
        prof["Languages"] = []
        for i in range(len(self.languages)):
            if self.languages[i]:
                prof["Languages"].append(
                    LanguageProficiency(i).name.title())

        return prof
