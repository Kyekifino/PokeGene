from Pokemon import Pokemon
import random
import math
from Types import types

# Creates and returns a Pokemon with random characteristics
def generate_random_pokemon():
    # I chose to represent each Pokemon's base stats, which will be normalized to a total of 600,
    # using a Gamma distribution. This will ensure that a Pokemon will never have negative stats,
    # and will tend to create similar but variable stat distributions. There are likely many other
    # great ways to generate these stats, but I liked this technique.
    stats = [math.floor(random.gammavariate(5, 20)) for x in range(0,6)]
    type_primary = random.choice(types)
    type_secondary = random.choice(types)
    move_type = random.choice(types)
    damage_category = random.choice(["Physical", "Special"])
    pokemon = Pokemon(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], type_primary, type_secondary, move_type, damage_category)
    print(pokemon)

for x in range(0, 100):
    generate_random_pokemon()
