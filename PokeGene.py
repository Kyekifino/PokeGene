from tkinter import *
from Pmw import Balloon
import GeneticAlgorithm as ga
import math
import threading

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
stop_run = threading.Event()

# Generate random set of Pokemon.
def generate_population():
    # Set button states
    global generate_population_button
    global next_generation_button
    global reset_button
    global auto_button
    global stop_button
    generate_population_button['state'] = DISABLED
    next_generation_button['state'] = NORMAL
    reset_button['state'] = NORMAL
    auto_button['state'] = NORMAL
    stop_button['state'] = DISABLED

    global pokemon_population
    pokemon_population = ga.create_new_population()
    fill_canvas()

# Run one step of the simulation.
def advance_generation():
    global generation_number
    global generation_number_label
    global pokemon_population
    generation_number = generation_number + 1
    generation_string.set("Generation: " + str(generation_number))
    pokemon_population = ga.run_genetic_algorithm_step(pokemon_population)
    fill_canvas()

# Empty the canvas, and reset the generation number
def reset_canvas():
    # Set button states
    global generate_population_button
    global next_generation_button
    global reset_button
    global auto_button
    global stop_button
    generate_population_button['state'] = NORMAL
    next_generation_button['state'] = DISABLED
    reset_button['state'] = DISABLED
    auto_button['state'] = DISABLED
    stop_button['state'] = DISABLED

    global generation_number
    global generation_number_label
    global pokemon_canvas
    global pokemon_population
    pokemon_population = []
    delete_list = pokemon_canvas.grid_slaves()
    for x in delete_list:
        x.destroy()
    generation_number = 0
    generation_string.set("Generation: " + str(generation_number))

# Update Pokemon Canvas with current Pokemon Population
def fill_canvas():
    global pokemon_population
    global pokemon_canvas
    delete_list = pokemon_canvas.grid_slaves()
    for x in delete_list:
        x.destroy()
    pokemon_population = sorted(pokemon_population, key = lambda x : x.age)
    rows = math.ceil(len(pokemon_population) / 10)
    pokemon_info = Balloon(pokemon_canvas)
    for r in range(rows):
        for c in range(10):
            pokemon = pokemon_population[10*r + c]
            pokemon_space = Canvas(pokemon_canvas, height = 34, width = 34, bg = type_colors[pokemon.type_primary], bd=1, highlightthickness=0, relief = RAISED)
            if pokemon.type_secondary is not None:
                pokemon_space.create_polygon(4, 0, 34, 0, 34, 30, fill = type_colors[pokemon.type_secondary])
            pokemon_space.create_oval(27, 2, 32, 7, fill = type_colors[pokemon.move_type])
            pokemon_info.bind(pokemon_space, str(pokemon))
            pokemon_space.grid(row = r, column = c)

#Automatically update the simulation on a certain timer
def auto_sim():
    # Set button states
    global generate_population_button
    global next_generation_button
    global reset_button
    global auto_button
    global stop_button
    global update_rate_entry
    generate_population_button['state'] = DISABLED
    next_generation_button['state'] = DISABLED
    reset_button['state'] = DISABLED
    auto_button['state'] = DISABLED
    stop_button['state'] = NORMAL
    update_rate_entry['state'] = DISABLED

    global stop_run
    global gui
    def run(stop_run, wait_time):
        if not stop_run.is_set():
            advance_generation()
            gui.after(wait_time, run, stop_run, wait_time)
    stop_run.clear()
    try:
        wait_time = int(float(update_rate_entry.get()) * 1000)
        run(stop_run, wait_time)
    except ValueError:
        print("Error: Update rate could not be parsed.")

# Stop auto-running the simulation
def stop_sim():
    # Set button states
    global generate_population_button
    global next_generation_button
    global reset_button
    global auto_button
    global stop_button
    global update_rate_entry
    generate_population_button['state'] = DISABLED
    next_generation_button['state'] = NORMAL
    reset_button['state'] = NORMAL
    auto_button['state'] = NORMAL
    stop_button['state'] = DISABLED
    update_rate_entry['state'] = NORMAL

    global stop_run
    stop_run.set()

# Fill the Pokemon Frame
population_label = Label(pokemon_frame, text = 'Current Population', bg = BG_COLOR)
pokemon_canvas = Frame(pokemon_frame, height = 364, width = 364, bg = FG_COLOR, bd = 2, relief = RIDGE)
population_label.pack(side = TOP)
pokemon_canvas.pack(side = TOP)

# Fill the Menu Frame
generation_number_label = Label(menu_frame, textvariable = generation_string, bg = BG_COLOR, relief = RIDGE)
generate_population_button = Button(menu_frame, text = 'Generate Random Population', bg = FG_COLOR, command = generate_population, state = NORMAL)
next_generation_button = Button(menu_frame, text = 'Next Generation', bg = FG_COLOR, command = advance_generation, state = DISABLED)
reset_button = Button(menu_frame, text = 'Reset', bg = FG_COLOR, command = reset_canvas, state = DISABLED)
update_rate_label = Label(menu_frame, text = 'Update Rate (seconds)', bg = BG_COLOR)
update_rate_entry = Entry(menu_frame)
update_rate_entry.insert(0, '1')
auto_button = Button(menu_frame, text = 'Run Simulation', bg = FG_COLOR, command = auto_sim, state = DISABLED)
stop_button = Button(menu_frame, text = 'Stop Simulation', bg = FG_COLOR, command = stop_sim, state = DISABLED)
generation_number_label.pack(side = TOP, fill = X, padx = 3, pady = 3)
generate_population_button.pack(side = TOP, fill = X, padx = 3, pady = 3)
next_generation_button.pack(side = TOP, fill = X, padx = 3)
reset_button.pack(side = TOP, fill = X, padx = 3, pady = 3)
update_rate_label.pack(side = TOP, fill = X, padx = 3)
update_rate_entry.pack(side = TOP, fill = X, padx = 3)
auto_button.pack(side = TOP, fill = X, padx = 3, pady = 3)
stop_button.pack(side = TOP, fill = X, padx = 3)

pokemon_frame.pack(side = LEFT)
menu_frame.pack(side = LEFT, fill = Y)

mainloop() # Start GUI execution
