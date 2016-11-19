from char_enum import Ability
from core.background import Background
from core.dnd_class import DnDClass
from core.race import Race

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
        self.race = Race()
        self.dnd_class = DnDClass()
        self.background = Background()
        self.equipment = None

        # description
        self.name = None
        self.player = None
        self.campaign = None
        self.gender = None
        self.age = None
        self.height = None
        self.weight = None
        self.hair = None
        self.eyes = None
        self.experience = 0
        self.notable_features = None
        self.image = None


    def getProficiency(self):
        prof = self.race.getProficiency()
        prof = self.dnd_class.getProficiency(proficiency=prof)
        prof = self.background.getProficiency(proficiency=prof)
        return prof

    # Strength
        
    def getStrength(self):
        return self.ability[Ability.strength]

    def setStrength(self, strength):
        if strength == '':
            self.ability[Ability.strength] = None
        else:
            self.ability[Ability.strength] = int(strength)

    # Dexterity

    def getDexterity(self):
        return self.ability[Ability.dexterity]

    def setDexterity(self, dex):
        if dex == '':
            self.ability[Ability.dexterity] = None
        else:
            self.ability[Ability.dexterity] = int(dex)

    # Constitution

    def getConstitution(self):
        return self.ability[Ability.constitution]

    def setConstitution(self, con):
        if con == '':
            self.ability[Ability.constitution] = None
        else:
            self.ability[Ability.constitution] = int(con)

    # Intelligence
        
    def getIntelligence(self):
        return self.ability[Ability.intelligence]

    def setIntelligence(self, intelligence):
        if intelligence == '':
            self.ability[Ability.intelligence] = None
        else:
            self.ability[Ability.intelligence] = int(intelligence)

    # Wisdom
    
    def getWisdom(self):
        return self.ability[Ability.wisdom]

    def setWisdom(self, wis):
        if wis == '':
            self.ability[Ability.wisdom] = None
        else:
            self.ability[Ability.wisdom] = int(wis)

    # Charisma

    def getCharisma(self):
        return self.ability[Ability.charisma]

    def setCharisma(self, cha):
        if cha == '':
            self.ability[Ability.charisma] = None
        else:
            self.ability[Ability.charisma] = int(cha)
            
    def setName(self, name):
        self.name = str(name)

    def setPlayer(self, player):
        self.player = str(player)

    def setCampaign(self, campaign):
        self.campaign = str(campaign)

    def setGender(self, gender):
        self.gender = str(gender)

    def setAge(self, age):
        self.age = int(age)

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setHair(self, hair):
        self.hair = hair

    def setEyes(self, eyes):
        self.eyes = eyes

    def setExperience(self, xp):
        self.experience = xp

    def setImage(self, image):
        self.image = image
        
    def write(self):
        print " Character\n"
        print "Name: ", self.name
        print "Player: ", self.player
        print "Campaign: ", self.campaign
        print "Gender: ", self.gender
        print "Age: ", self.age
        print "Height: ", self.height
        print "Weight: ", self.weight
        print "Hair: ", self.hair
        print "Eyes: ", self.eyes
        print "XP: ", self.experience
        print "Notable Features: ", self.notable_features
        print "Image: ", self.image

        name = ["Strength: ", "Dexterity: ", "Constitution: ",
                "Intelligence: ", "Wisdom: ", "Charisma: "]
        for i in range(len(name)):
            print name[i], self.ability[i]

        print "\n RACE\n"
        if self.race is not None:
            self.race.write()

        print "\n CLASS\n"
        if self.dnd_class is not None:
            self.dnd_class.write()
            
        print "\n BACKGROUND\n"
        if self.background is not None:
            self.background.write()
