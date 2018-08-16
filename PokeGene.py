from tkinter import *
import GeneticAlgorithm as ga

BG_COLOR = '#9999ff'
FG_COLOR = '#6666ff'

# Chart of type-related colors.
type_colors = {"Normal": '#ada594', "Fire": '#f75231', "Water": '#399cff', "Electric": '#ffc631',
             "Grass": '#7bce52', "Ice": '#5acee7', "Fighting": '#a55239', "Poison": '#b55aa5',
             "Ground": '#d6b55a', "Flying": '#9cadf7', "Psychic": '#ff73a5', "Bug": '#adbd21',
             "Rock": '#bda55a', "Ghost": '#6363b5', "Dragon": '#7b63e7', "Dark": '#735a4a',
             "Steel": '#adadc6', "Fairy": '#f7b5f7'
             }

gui = Tk() # Initialize GUI

generation_number = 0
generation_string = StringVar()
generation_string.set("Generation: " + str(generation_number))
gui.title("PokeGene")
gui.configure(background = BG_COLOR)
pokemon_population = []
pokemon_frame = Frame(gui, bg = BG_COLOR,)
menu_frame = Frame(gui, bg = BG_COLOR, bd = 2, relief = RIDGE)

# Generate random set of Pokemon.
def generate_population():
    global pokemon_population
    pokemon_population = ga.generate_random_pokemon()
    # TODO: Update Pokemon Canvas with Pokemon

# Run one step of the simulation.
def advance_generation():
    global generation_number
    global generation_number_label
    generation_number = generation_number + 1
    generation_string.set("Generation: " + str(generation_number))
    # TODO: Run step on Pokemon Population

# Fill the Pokemon Frame
population_label = Label(pokemon_frame, text = 'Current Population', bg = BG_COLOR)
pokemon_canvas = Frame(pokemon_frame, height = 500, width = 500, bg = FG_COLOR, bd = 2, relief = RIDGE)
population_label.pack(side = TOP)
pokemon_canvas.pack(side = TOP)

# Fill the Menu Frame
generation_number_label = Label(menu_frame, textvariable = generation_string, bg = BG_COLOR, relief = RIDGE)
generate_population_button = Button(menu_frame, text = 'Generate Random Population', bg = FG_COLOR, command = generate_population)
next_generation_button = Button(menu_frame, text = 'Next Generation', bg = FG_COLOR, command = advance_generation)
reset_button = Button(menu_frame, text = 'Reset', bg = FG_COLOR)
update_rate_label = Label(menu_frame, text = 'Update Rate (seconds)', bg = BG_COLOR)
update_rate_entry = Entry(menu_frame)
update_rate_entry.insert(0, '1')
auto_button = Button(menu_frame, text = 'Run Simulation', bg = FG_COLOR)
generation_number_label.pack(side = TOP, fill = X, padx = 3, pady = 3)
generate_population_button.pack(side = TOP, fill = X, padx = 3, pady = 3)
next_generation_button.pack(side = TOP, fill = X, padx = 3)
reset_button.pack(side = TOP, fill = X, padx = 3, pady = 3)
update_rate_label.pack(side = TOP, fill = X, padx = 3)
update_rate_entry.pack(side = TOP, fill = X, padx = 3)
auto_button.pack(side = TOP, fill = X, padx = 3, pady = 3)

pokemon_frame.pack(side = LEFT)
menu_frame.pack(side = LEFT, fill = Y)

mainloop() # Start GUI execution
