from enum import Enum

class Proficiency(Enum):
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

class ObjectProficiency():
    def __init__(self):
        self.weapons = [False]*38
        self.tools = [False]*3
        self.armors = [False]*39

    def addWeaponProficiency(self, prof):
        for i in prof_list:
            if prof == "simple":
                self.proficiency[0:15] = True
            elif prof == "martial":
                self.proficiency[15:0] = True
            else:
                self.proficiency[prof] = True

    def addArmorProficiency(self, prof):
        self.proficiency[prof] = True

    def addToolProficiency(self, prof):
        self.proficiency[prof] = True
