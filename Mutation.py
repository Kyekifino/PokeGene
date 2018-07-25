from functools import partial

def mutate_stats(gained_stat, lost_stat, pokemon):
    if pokemon.__dict__[lost_stat] > 10:
        pokemon.__dict__.gained_stat += 10
        pokemon.__dict__.lost_stat -= 10
        pokemon.recalculate_stats()

# List of possible Pokemon mutations
mutation_list = {
                 'Hardy' : partial(mutate_stats, "base_hp", "base_attack"), # +HP, -Atk
                 'Docile' : partial(mutate_stats, "base_hp", "base_defense"), # +HP, -Def
                 'Serious' : partial(mutate_stats, "base_hp", "base_speed"), # +HP, -Spd
                 'Bashful' : partial(mutate_stats, "base_hp", "base_special_attack"), # +HP, -SpA
                 'Quirky' : partial(mutate_stats, "base_hp", "base_special_defense"), # +HP, -SpD
                 'Strong' : partial(mutate_stats, "base_attack", "base_hp"), # +Atk, -HP
                 'Lonely' : partial(mutate_stats, "base_attack", "base_defense"), # +Atk, -Def
                 'Brave' : partial(mutate_stats, "base_attack", "base_speed"), # +Atk, -Spd
                 'Adamant' : partial(mutate_stats, "base_attack", "base_special_attack"), # +Atk, -SpA
                 'Naughty' : partial(mutate_stats, "base_attack", "base_special_defense"), # +Atk, -SpD
                 'Constitute' : partial(mutate_stats, "base_defense", "base_hp"), # +Def, -HP
                 'Bold' : partial(mutate_stats, "base_defense", "base_attack"), # +Def, -Atk
                 'Relaxed' : partial(mutate_stats, "base_defense", "base_speed"), # +Def, -Spd
                 'Impish' : partial(mutate_stats, "base_defense", "base_special_attack"), # +Def, -SpA
                 'Lax' : partial(mutate_stats, "base_defense", "base_special_defense"), # +Def, -SpD
                 'Dexterous' : partial(mutate_stats, "base_speed", "base_hp"), # +Spd, -HP
                 'Timid' : partial(mutate_stats, "base_speed", "base_attack"), # +Spd, -Atk
                 'Hasty' : partial(mutate_stats, "base_speed", "base_defense"), # +Spd, -Def
                 'Jolly' : partial(mutate_stats, "base_speed", "base_special_attack"), # +Spd, -SpA
                 'Naive' : partial(mutate_stats, "base_speed", "base_special_defense"), # +Spd, -SpD
                 'Intelligent' : partial(mutate_stats, "base_special_attack", "base_hp"), # +SpA, -HP
                 'Modest' : partial(mutate_stats, "base_special_attack", "base_attack"), # +SpA, -Atk
                 'Mild' : partial(mutate_stats, "base_special_attack", "base_defense"), # +SpA, -Def
                 'Quiet' : partial(mutate_stats, "base_special_attack", "base_speed"), # +SpA, -Spd
                 'Rash' : partial(mutate_stats, "base_special_attack", "base_special_defense"), # +SpA, -SpD
                 'Wise' : partial(mutate_stats, "base_special_defense", "base_hp"), # +SpD, -HP
                 'Calm' : partial(mutate_stats, "base_special_defense", "base_attack"), # +SpD, -Atk
                 'Gentle' : partial(mutate_stats, "base_special_defense", "base_defense"), # +SpD, -Def
                 'Sassy' : partial(mutate_stats, "base_special_defense", "base_speed"), # +SpD, -Spd
                 'Careful' : partial(mutate_stats, "base_special_defense", "base_special_attack"), # +SpD, -SpA
                 'Primary Type' : mutate_primary_type,
                 'Secondary Type' : mutate_secondary_type,
                 'Move Type' : mutate_move_type,
                 'Damage Category' : mutate_damage_category
                }
