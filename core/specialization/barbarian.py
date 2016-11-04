import char_enum
import equipment.basic_weapon
import equipment.pack

class Barbarian:
    def __init__(self):
        # type of dice
        self.hit_dice = 12
        self.hit_point = 12
        # text advantage
        self.advantage = []
        self.advantage.append("Rage")
        self.advantage.append("Unarmored Defense")
        # proficiencies
        self.saving_throws = (char_enum.Ability.strength)
        self.object_proficiency = proficiency.ObjectProficiency()
        self.object_proficiency.addWeaponProficiency(
            ["Simple", "martial"])

        # tools proficiencies choosen
        self.tools_proficiency = None
        # languages
        self.languages = ["Common", "Dwarvish"]
        # subraces
        self.subrace = ["HillDwarf", "MountainDwarf"]
        # equipement
        self.equipement_choice = []
        # choices
        self.equipment_choice.append(
            (basic_weapon.GreatAxe(), "martial"))
        self.equipment_choice.append(
            ([basic_weapon.HandAxe]*2, "simple"))
        self.equipment_choice.append(
            [pack.ExplorerPack(), [basic_weapon.Javelin]*4])

    def getSkillsChoice(self):
        """ return a tuple (number of choice, list of choice)
        """
        choice = [
            proficiency.Proficiency.animal_handling,
            proficiency.Proficiency.athletics,
            proficiency.Proficiency.intimidation,
            proficiency.Proficiency.nature,
            proficiency.Proficiency.perception,
            proficiency.Proficiency.survival]
        return (2,choice)
        
    def setSkillsChoice(self, choice):
        self.skills_choosen = choice


    def levelUp(self):
        self.hit_point += 7
