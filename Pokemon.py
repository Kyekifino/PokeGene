import math

# Configure the max number for base stat total here.
BASE_STAT_MAX = 600

# Chart of type weaknesses. type_dict["Water"]["Fire"] assumes water is attacking fire.
type_dict = {"Normal": {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":1, "Poison":1, "Ground":1, "Flying":1, "Psychic":1, "Bug":1, "Rock":0.5, "Ghost":0, "Dragon":1, "Dark":1, "Steel":0.5, "Fairy":1},
             "Fire": {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":1, "Grass":2, "Ice":2, "Fighting":1, "Poison":1, "Ground":1, "Flying":1, "Psychic":1, "Bug":2, "Rock":0.5, "Ghost":1, "Dragon":0.5, "Dark":1, "Steel":2, "Fairy":1},
             "Water": {"Normal":1, "Fire":2, "Water":0.5, "Electric":1, "Grass":0.5, "Ice":1, "Fighting":1, "Poison":1, "Ground":2, "Flying":1, "Psychic":1, "Bug":1, "Rock":2, "Ghost":1, "Dragon":0.5, "Dark":1, "Steel":1, "Fairy":1},
             "Electric": {"Normal":1, "Fire":1, "Water":2, "Electric":0.5, "Grass":0.5, "Ice":1, "Fighting":1, "Poison":1, "Ground":0, "Flying":2, "Psychic":1, "Bug":1, "Rock":1, "Ghost":1, "Dragon":0.5, "Dark":1, "Steel":1, "Fairy":1},
             "Grass": {"Normal":1, "Fire":0.5, "Water":2, "Electric":1, "Grass":0.5, "Ice":1, "Fighting":1, "Poison":0.5, "Ground":2, "Flying":0.5, "Psychic":1, "Bug":0.5, "Rock":2, "Ghost":1, "Dragon":0.5, "Dark":1, "Steel":0.5, "Fairy":1},
             "Ice": {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":1, "Grass":2, "Ice":0.5, "Fighting":1, "Poison":1, "Ground":2, "Flying":2, "Psychic":1, "Bug":1, "Rock":1, "Ghost":1, "Dragon":2, "Dark":1, "Steel":0.5, "Fairy":1},
             "Fighting": {"Normal":2, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":2, "Fighting":1, "Poison":0.5, "Ground":2, "Flying":0.5, "Psychic":0.5, "Bug":0.5, "Rock":2, "Ghost":0, "Dragon":1, "Dark":2, "Steel":2, "Fairy":0.5},
             "Poison": {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":2, "Ice":1, "Fighting":1, "Poison":0.5, "Ground":0.5, "Flying":1, "Psychic":1, "Bug":1, "Rock":0.5, "Ghost":0.5, "Dragon":1, "Dark":1, "Steel":0, "Fairy":2},
             "Ground": {"Normal":1, "Fire":2, "Water":1, "Electric":2, "Grass":0.5, "Ice":1, "Fighting":1, "Poison":2, "Ground":1, "Flying":0, "Psychic":1, "Bug":0.5, "Rock":2, "Ghost":1, "Dragon":1, "Dark":1, "Steel":2, "Fairy":1},
             "Flying": {"Normal":1, "Fire":1, "Water":1, "Electric":0.5, "Grass":2, "Ice":1, "Fighting":2, "Poison":1, "Ground":1, "Flying":1, "Psychic":1, "Bug":2, "Rock":0.5, "Ghost":1, "Dragon":1, "Dark":1, "Steel":0.5, "Fairy":1},
             "Psychic": {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":2, "Poison":2, "Ground":1, "Flying":1, "Psychic":0.5, "Bug":1, "Rock":1, "Ghost":1, "Dragon":1, "Dark":0, "Steel":0.5, "Fairy":1},
             "Bug": {"Normal":1, "Fire":0.5, "Water":1, "Electric":1, "Grass":2, "Ice":1, "Fighting":0.5, "Poison":0.5, "Ground":1, "Flying":0.5, "Psychic":2, "Bug":1, "Rock":1, "Ghost":0.5, "Dragon":1, "Dark":2, "Steel":0.5, "Fairy":0.5},
             "Rock": {"Normal":1, "Fire":2, "Water":1, "Electric":1, "Grass":1, "Ice":2, "Fighting":0.5, "Poison":1, "Ground":0.5, "Flying":2, "Psychic":1, "Bug":2, "Rock":1, "Ghost":1, "Dragon":1, "Dark":1, "Steel":0.5, "Fairy":1},
             "Ghost": {"Normal":0, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":1, "Poison":1, "Ground":1, "Flying":1, "Psychic":2, "Bug":1, "Rock":1, "Ghost":2, "Dragon":1, "Dark":0.5, "Steel":1, "Fairy":1},
             "Dragon": {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":1, "Poison":1, "Ground":1, "Flying":1, "Psychic":1, "Bug":1, "Rock":1, "Ghost":1, "Dragon":2, "Dark":1, "Steel":0.5, "Fairy":0},
             "Dark": {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":0.5, "Poison":1, "Ground":1, "Flying":1, "Psychic":2, "Bug":1, "Rock":1, "Ghost":2, "Dragon":1, "Dark":0.5, "Steel":1, "Fairy":0.5},
             "Steel": {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":0.5, "Grass":1, "Ice":2, "Fighting":1, "Poison":1, "Ground":1, "Flying":1, "Psychic":1, "Bug":1, "Rock":2, "Ghost":1, "Dragon":1, "Dark":1, "Steel":0.5, "Fairy":1},
             "Fairy": {"Normal":1, "Fire":0.5, "Water":1, "Electric":1, "Grass":1, "Ice":1, "Fighting":2, "Poison":0.5, "Ground":1, "Flying":1, "Psychic":1, "Bug":1, "Rock":1, "Ghost":1, "Dragon":2, "Dark":2, "Steel":0.5, "Fairy":1}
             }

# Returns the multiplier for damage on an attack against a Pokemon.
def damage_mult(attacking_move_type, attacked_pokemon_type_primary, attacked_pokemon_type_secondary = None):
    multiplier = type_dict[attacking_move_type][attacked_pokemon_type_primary]
    if attacked_pokemon_type_secondary is not None:
        multiplier *= type_dict[attacking_move_type][attacked_pokemon_type_secondary]
    return multiplier

# Class to abstractly represent a Pokemon
class Pokemon:

    def __init__(self, hp, attack, defense, special_attack, special_defense, speed, type_primary="Normal", type_secondary=None, move_type="Normal", damage_category="Physical"):
        # For fairness sake, make sure all Pokemon have a cap on max stats.
        total_stats = hp + attack + defense + special_attack + special_defense + speed
        if total_stats > BASE_STAT_MAX:
            adjustment_factor = (BASE_STAT_MAX/total_stats)
        else:
            adjustment_factor = 1
        self.hp = math.floor(hp*adjustment_factor)
        self.attack = math.floor(attack*adjustment_factor)
        self.defense = math.floor(defense*adjustment_factor)
        self.special_attack = math.floor(special_attack*adjustment_factor)
        self.special_defense = math.floor(special_defense*adjustment_factor)
        self.speed = math.floor(speed*adjustment_factor)
        # Set Types. Secondary type may be None
        self.type_primary = type_primary
        self.type_secondary = type_secondary
        self.move_type = move_type
        self.damage_category = damage_category

    def __str__(self):
        pokemon_string = self.type_primary
        if self.type_secondary is not None:
            pokemon_string += "/" + self.type_secondary
        pokemon_string += " [" + self.move_type + "]"
        pokemon_string += "\nHP: " + str(self.hp)
        pokemon_string += "\nAtk: " + str(self.attack)
        pokemon_string += "\nDef: " + str(self.defense)
        pokemon_string += "\nSpA: " + str(self.special_attack)
        pokemon_string += "\nSpD: " + str(self.special_defense)
        pokemon_string += "\nSpd: " + str(self.speed)
        return pokemon_string
