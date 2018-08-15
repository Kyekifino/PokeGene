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

gui.title("PokeGene")
pokemon_population = ga.create_new_population()
pokemon_frame = Frame(gui, bg = BG_COLOR)
menu_frame = Frame(gui, bg = BG_COLOR)

# Fill the Pokemon Frame
population_label = Label(pokemon_frame, text = 'Current Population', bg = BG_COLOR)
pokemon_canvas = Canvas(pokemon_frame, height = 500, width = 500, bg = FG_COLOR)
population_label.pack(side = TOP)
pokemon_canvas.pack(side = TOP)

# Fill the Menu Frame
next_generation_button = Button(menu_frame, text = 'Advance Generation...', bg = FG_COLOR)
next_generation_button.pack(side = TOP)

pokemon_frame.pack(side = LEFT)
menu_frame.pack(side = LEFT)

mainloop() # Start GUI execution
