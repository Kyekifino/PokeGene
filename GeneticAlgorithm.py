from Pokemon import Pokemon, battle_pokemon, breed_pokemon
import random
import math
from Types import types
from itertools import zip_longest

# Shamelessly taken from the itertools recipes on https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

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
    return pokemon

# Create new population of some number of random Pokemon.
def create_new_population(size = 100):
    population = [generate_random_pokemon() for x in range(0, size)]
    return population

# Runs one discrete step of the genetic algorithm.
# Tests fitness by killing the Pokemon that loses in a randomly selected battle.
# Breeds new Pokemon from the victors.
# Mutates these new Pokemon before adding them to the final population.
def run_genetic_algorithm_step(population):
    # Randomize the order of the population
    random.shuffle(population)
    halved_population = []
    for x,y in grouper(population, 2):
        halved_population.append(battle_pokemon(x, y)[0])
    baby_population = []
    for father in halved_population:
        mother = random.choice(halved_population)
        baby = breed_pokemon(father, mother)
        baby.mutate()
        baby_population.append(baby)
    new_population = halved_population + baby_population
    return new_population

# Just a toy example to play with for now. Noticibly solid variability in which
# Pokemon reign after running it a few times. Try it out! The next goal is to add
# a UI to it.
pop = run_genetic_algorithm_step(create_new_population())
for x in range(1000):
    pop = run_genetic_algorithm_step(pop)
for x in pop:
    print(x)
