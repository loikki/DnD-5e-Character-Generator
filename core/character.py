from core.proficiency import Ability
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

    def heal(self, value, dice):
        hit, max_hit = self.getHitPoint()
        self.dnd_class.hit_dice -= dice
        if hit + value <= max_hit:
            self.dnd_class.hit_point += value
        else:
            self.dnd_class.hit_point = max_hit

    def getHitDice(self):
        hit_dice = [None]*3
        hit_dice[0], hit_dice[2] = self.dnd_class.getHitDice()
        hit_dice[1] = getLevel(self.experience)
        return hit_dice

    def addHitDice(self, new_hit_dice):
        cur, max_hit, temp = self.getHitDice()
        if cur + new_hit_dice <= max_hit:
            self.dnd_class.hit_dice += new_hit_dice
        else:
            self.dnd_class.hit_dice = max_hit
        
    def setHitPoint(self):
        """ Set the initial hit points
        """
        self.dnd_class.setHitPoint()
        self.dnd_class.hit_point += getLevel(
            self.experience)*getModifier(self.getConstitution())
        
    def getHitPoint(self):
        """
        :returns: (current, max)
        """
        max_hit = self.dnd_class.max_hit_point
        # take into account the constitution modifiers
        max_hit += getLevel(self.experience)*getModifier(
            self.getConstitution())
        return self.dnd_class.hit_point, max_hit

    def getProficiency(self):
        prof, diff = self.race.getProficiency()
        prof, temp = self.dnd_class.getProficiency(proficiency=prof)
        if not temp:
            diff = temp
        prof, temp = self.background.getProficiency(proficiency=prof)
        if not temp:
            diff = temp
        return prof, diff

    # Strength
        
    def getStrength(self):
        return self.ability[Ability.strength.value]

    def setStrength(self, strength):
        if strength == '':
            self.ability[Ability.strength.value] = None
        else:
            self.ability[Ability.strength.value] = int(strength)

    # Dexterity

    def getDexterity(self):
        return self.ability[Ability.dexterity.value]

    def setDexterity(self, dex):
        if dex == '':
            self.ability[Ability.dexterity.value] = None
        else:
            self.ability[Ability.dexterity.value] = int(dex)

    # Constitution

    def getConstitution(self):
        return self.ability[Ability.constitution.value]

    def setConstitution(self, con):
        if con == '':
            self.ability[Ability.constitution.value] = None
        else:
            self.ability[Ability.constitution.value] = int(con)

    # Intelligence
        
    def getIntelligence(self):
        return self.ability[Ability.intelligence.value]

    def setIntelligence(self, intelligence):
        if intelligence == '':
            self.ability[Ability.intelligence.value] = None
        else:
            self.ability[Ability.intelligence.value] = int(intelligence)

    # Wisdom
    
    def getWisdom(self):
        return self.ability[Ability.wisdom.value]

    def setWisdom(self, wis):
        if wis == '':
            self.ability[Ability.wisdom.value] = None
        else:
            self.ability[Ability.wisdom.value] = int(wis)

    # Charisma

    def getCharisma(self):
        return self.ability[Ability.charisma.value]

    def setCharisma(self, cha):
        if cha == '':
            self.ability[Ability.charisma.value] = None
        else:
            self.ability[Ability.charisma.value] = int(cha)
            
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
