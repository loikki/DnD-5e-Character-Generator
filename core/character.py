import char_enum

XP_LIMITS = [300, 900, 2700, 6500, 14000, 23000, 34000, 48000,
             64000, 85000, 100000, 120000, 140000, 165000, 195000,
             225000, 265000, 305000, 355000]

def getModifier(att):
    return (att - 10)/2

def getXPLimit(lvl):
    return XP_LIMITS[lvl-1]

def getLevel(xp):
    for i in range(len(XP_LIMITS)):
        if XP_LIMITS[i] > xp:
            return i+1

def proficiencyBonus(lvl):
    if lvl < 5:
        return 2
    elif lvl < 9:
        return 3
    elif lvl < 13:
        return 4
    elif lvl < 17:
        return 5
    else:
        return 6

class Character:
    def __init__(self):
        self.ability = [0]*6
        self.lvl = 1

        # Origin
        self.race = None
        self.subrace = None
        self.specialization = None
        self.background = None
        self.equipment = None

        self.alignment = None

    def levelUp(self):
        self.specialization.LevelUp()

    def setRace(self, race_name):
        self.race = race(race_name)
