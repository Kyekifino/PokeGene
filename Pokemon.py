import math
import random
import Mutation

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

# Returns the damage dealt to a Pokemon by an attack
def calculate_damage(attacking_pokemon, defending_pokemon, use_random=True):
    level = attacking_pokemon.level
    power = 60 # May update with more moves later, for now it'll be stuck to 60
    if attacking_pokemon.damage_category == "Physical":
        attack = attacking_pokemon.attack
        defense = defending_pokemon.defense
    elif attacking_pokemon.damage_category == "Special":
        attack = attacking_pokemon.special_attack
        defense = defending_pokemon.special_defense
    else:
        raise ValueError("Attacking Pokemon must be Physical or Special in damage category.")
    # Calculate the modifier
    # TODO: May want to add weather, criticals
    if use_random:
        random_spread = random.randint(217,255)
        random_spread /= 255
    else:
        random_spread = 1
    if attacking_pokemon.type_primary == attacking_pokemon.move_type or attacking_pokemon.type_secondary == attacking_pokemon.move_type:
        stab = 1.5
    else:
        stab = 1
    type = damage_mult(attacking_pokemon.move_type, defending_pokemon.type_primary, defending_pokemon.type_secondary)
    multiplier = random_spread * stab * type
    # Calculate the damage
    damage = math.floor((((((2*level)/5) + 2) * power * attack / defense) / 50 + 2) * multiplier)
    return damage

# Returns the victorious Pokemon in a simulated battle between the two, as well as the duration of the battle. Returns a random winner if neither can effect one another
def battle_pokemon(pokemon_one, pokemon_two, use_random=True):
    # Decide randomly if neither can fight.
    if damage_mult(pokemon_one.move_type, pokemon_two.type_primary, pokemon_two.type_secondary) == 0 and damage_mult(pokemon_two.move_type, pokemon_one.type_primary, pokemon_one.type_secondary) == 0:
        if random.random() > 0.5:
            return pokemon_one, 0
        else:
            return pokemon_two, 0
    pokemon_one.current_hp = pokemon_one.hp
    pokemon_two.current_hp = pokemon_two.hp
    turn_num = 1
    while True:
        # Implemented this way to ease inclusion of Statuses and Stat changing moves in the future.
        battle_order = []
        battle_order.append(pokemon_one)
        battle_order.append(pokemon_two)
        # Sorts by highest speed first
        battle_order.sort(key= lambda pokemon: pokemon.speed, reverse=True)
        battle_order[1].current_hp -= calculate_damage(battle_order[0], battle_order[1], use_random)
        if battle_order[1].current_hp <= 0:
            del battle_order[0].__dict__["current_hp"]
            return battle_order[0], turn_num
        battle_order[0].current_hp -= calculate_damage(battle_order[1], battle_order[0], use_random)
        if battle_order[0].current_hp <= 0:
            del battle_order[1].__dict__["current_hp"]
            return battle_order[1], turn_num
        turn_num += 1

# Create a new Pokemon with traits randomly selected from the father and mother.
def breed_pokemon(father, mother):
    base_hp = random.choice([father.base_hp, mother.base_hp])
    base_attack = random.choice([father.base_attack, mother.base_attack])
    base_defense = random.choice([father.base_defense, mother.base_defense])
    base_special_attack = random.choice([father.base_special_attack, mother.base_special_attack])
    base_special_defense = random.choice([father.base_special_defense, mother.base_special_defense])
    base_speed = random.choice([father.base_speed, mother.base_speed])
    type_primary = random.choice([father.type_primary, mother.type_primary])
    type_secondary = random.choice([father.type_secondary, mother.type_secondary])
    move_type = random.choice([father.move_type, mother.move_type])
    damage_category = random.choice([father.damage_category, mother.damage_category])
    child = Pokemon(base_hp, base_attack, base_defense, base_special_attack, base_special_defense, base_speed, type_primary, type_secondary, move_type, damage_category)
    return child

# Class to abstractly represent a Pokemon
class Pokemon:
    def __init__(self, hp, attack, defense, special_attack, special_defense, speed, type_primary="Normal", type_secondary=None, move_type="Normal", damage_category="Physical", level=50):
        # For fairness sake, make sure all Pokemon have a cap on max stats.
        total_stats = hp + attack + defense + special_attack + special_defense + speed
        if total_stats > BASE_STAT_MAX:
            adjustment_factor = (BASE_STAT_MAX/total_stats)
        else:
            adjustment_factor = 1
        self.base_hp = math.floor(hp*adjustment_factor)
        self.base_attack = math.floor(attack*adjustment_factor)
        self.base_defense = math.floor(defense*adjustment_factor)
        self.base_special_attack = math.floor(special_attack*adjustment_factor)
        self.base_special_defense = math.floor(special_defense*adjustment_factor)
        self.base_speed = math.floor(speed*adjustment_factor)
        # Set Types. Secondary type may be None
        self.type_primary = type_primary
        if type_primary == type_secondary:
            self.type_secondary = None
        else:
            self.type_secondary = type_secondary
        self.move_type = move_type
        self.damage_category = damage_category
        self.level = level
        # Calculate stats based on level. Assume no EVs, neutral nature and perfect IVs for now.
        self.recalculate_stats()

    def recalculate_stats(self):
        self.hp = math.floor(((((2*self.base_hp) + 31) * self.level)/100) + self.level + 10)
        self.attack = math.floor(((((2*self.base_attack) + 31) * self.level)/100) + 5)
        self.defense = math.floor(((((2*self.base_defense) + 31) * self.level)/100) + 5)
        self.special_attack = math.floor(((((2*self.base_special_attack) + 31) * self.level)/100) + 5)
        self.special_defense = math.floor(((((2*self.base_special_defense) + 31) * self.level)/100) + 5)
        self.speed = math.floor(((((2*self.base_speed) + 31) * self.level)/100) + 5)

    # Mutate a Pokemon at random.
    def mutate(self, mutation=None):
        if mutation is None:
            mutation = random.choice(list(Mutation.mutation_list.keys()))
        Mutation.mutation_list[mutation](self)

    def __repr__(self):
        pokemon_string = self.type_primary
        if self.type_secondary is not None:
            pokemon_string += "/" + self.type_secondary
        pokemon_string += " [" + self.move_type + "]"
        pokemon_string += " [" + str(self.hp)
        pokemon_string += "/" + str(self.attack)
        pokemon_string += "/" + str(self.defense)
        pokemon_string += "/" + str(self.special_attack)
        pokemon_string += "/" + str(self.special_defense)
        pokemon_string += "/" + str(self.speed) + "]"
        pokemon_string += " <" + self.damage_category + ">"
        return pokemon_string

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
