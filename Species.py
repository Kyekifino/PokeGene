import SpeciesNames
import random
import math

# Dictionary that contains all species in the simulation
species_pokedex = {}

# Return a random Pokemon species name
def getName(type_primary, type_secondary):
    prefix = random.choice(SpeciesNames.prefix_dict[type_primary])
    if type_secondary == None:
        suffix = random.choice(SpeciesNames.suffix_dict[type_primary])
    else:
        suffix = random.choice(SpeciesNames.suffix_dict[type_secondary])
    return prefix + suffix

# Class to abstractly represent a species of Pokemon
class Species:
    def __init__(self, hp, attack, defense, special_attack, special_defense, speed, type_primary="Normal", type_secondary=None):
        self.base_hp = math.floor(hp)
        self.base_attack = math.floor(attack)
        self.base_defense = math.floor(defense)
        self.base_special_attack = math.floor(special_attack)
        self.base_special_defense = math.floor(special_defense)
        self.base_speed = math.floor(speed)
        # Set Types. Secondary type may be None
        self.type_primary = type_primary
        self.type_secondary = type_secondary
        # Set name.
        self.name = getName(type_primary, type_secondary)
        while self.name in species_pokedex.keys():
            self.name = getName(type_primary, type_secondary)

    # Returns true if a Pokemon is a member of this species
    def isMember(self, Pokemon):
        if self.type_primary != Pokemon.type_primary:
            return False
        if self.type_secondary != Pokemon.type_secondary:
            return False
        if abs(self.base_hp - Pokemon.base_hp) > 20:
            return False
        if abs(self.base_attack - Pokemon.base_attack) > 20:
            return False
        if abs(self.base_defense - Pokemon.base_defense) > 20:
            return False
        if abs(self.base_special_attack - Pokemon.base_special_attack) > 20:
            return False
        if abs(self.base_special_defense - Pokemon.base_special_defense) > 20:
            return False
        if abs(self.base_speed - Pokemon.base_speed) > 20:
            return False
        return True
