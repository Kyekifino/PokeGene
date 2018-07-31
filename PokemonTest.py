import Pokemon as pok
import unittest

class TestDamageMult(unittest.TestCase):
    """
    Test the damage multiplier function from the Pokemon library
    """

    def test_super_duper_effective(self):
        """
        Test that attacking with 4x effectiveness will produce a 4
        """
        result = pok.damage_mult('Fire', 'Ice', 'Grass')
        self.assertEqual(result, 4)

    def test_super_effective(self):
        """
        Test that attacking with 2x effectiveness will produce a 2
        """
        result = pok.damage_mult('Water', 'Rock')
        self.assertEqual(result, 2)

    def test_effective(self):
        """
        Test that attacking with 1x effectiveness will produce a 1
        """
        result = pok.damage_mult('Fighting', 'Fire')
        self.assertEqual(result, 1)

    def test_effective_cancel(self):
        """
        Test that attacking with 2x and 0.5x effectiveness will produce a 1
        """
        result = pok.damage_mult('Fighting', 'Normal', 'Poison')
        self.assertEqual(result, 1)

    def test_not_very_effective(self):
        """
        Test that attacking with 0.5x effectiveness will produce a 0.5
        """
        result = pok.damage_mult('Normal', 'Steel')
        self.assertEqual(result, 0.5)

    def test_not_at_all_effective(self):
        """
        Test that attacking with 0.25x effectiveness will produce a 0.25
        """
        result = pok.damage_mult('Dark', 'Dark', 'Fairy')
        self.assertEqual(result, 0.25)

    def test_immune(self):
        """
        Test that attacking with 0x effectiveness will produce a 0
        """
        result = pok.damage_mult('Ground', 'Flying')
        self.assertEqual(result, 0)

class TestPokemonInit(unittest.TestCase):
    """
    Test the initializer function and string function from the Pokemon library
    """

    def test_base_600(self):
        """
        Test that a Pokemon with 600 stats works as intended
        """
        Mew = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Psychic')
        self.assertEqual(Mew.base_hp, 100)
        self.assertEqual(Mew.base_attack, 100)
        self.assertEqual(Mew.base_defense, 100)
        self.assertEqual(Mew.base_special_attack, 100)
        self.assertEqual(Mew.base_special_defense, 100)
        self.assertEqual(Mew.base_speed, 100)
        self.assertEqual(Mew.type_primary, 'Psychic')
        self.assertEqual(Mew.type_secondary, None)
        self.assertEqual(Mew.move_type, 'Normal')
        self.assertEqual(Mew.damage_category, 'Physical')
        self.assertEqual(Mew.level, 50)

        MewString = 'Psychic [Normal] [175/120/120/120/120/120] <Physical>'

        self.assertEqual(MewString, str(Mew))


    def test_all_fields(self):
        """
        Test that a Pokemon with all fields showing works as intended
        """
        Victini = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Psychic', 'Fire', 'Special', 100)
        self.assertEqual(Victini.base_hp, 100)
        self.assertEqual(Victini.base_attack, 100)
        self.assertEqual(Victini.base_defense, 100)
        self.assertEqual(Victini.base_special_attack, 100)
        self.assertEqual(Victini.base_special_defense, 100)
        self.assertEqual(Victini.base_speed, 100)
        self.assertEqual(Victini.type_primary, 'Fire')
        self.assertEqual(Victini.type_secondary, 'Psychic')
        self.assertEqual(Victini.move_type, 'Fire')
        self.assertEqual(Victini.damage_category, 'Special')
        self.assertEqual(Victini.level, 100)

        VictiniString = 'Fire/Psychic [Fire] [341/236/236/236/236/236] <Special>'

        self.assertEqual(VictiniString, str(Victini))

    def test_op(self):
        """
        Test that a Pokemon with over 600 stats works as intended
        """
        Strongo = pok.Pokemon(150, 150, 150, 150, 150, 40, 'Fighting')
        self.assertEqual(Strongo.base_hp, 113)
        self.assertEqual(Strongo.base_attack, 113)
        self.assertEqual(Strongo.base_defense, 113)
        self.assertEqual(Strongo.base_special_attack, 113)
        self.assertEqual(Strongo.base_special_defense, 113)
        self.assertEqual(Strongo.base_speed, 30)
        self.assertEqual(Strongo.type_primary, 'Fighting')
        self.assertEqual(Strongo.type_secondary, None)
        self.assertEqual(Strongo.move_type, 'Normal')
        self.assertEqual(Strongo.damage_category, 'Physical')
        self.assertEqual(Strongo.level, 50)

        StrongoString = 'Fighting [Normal] [188/133/133/133/133/50] <Physical>'

        self.assertEqual(StrongoString, str(Strongo))

    def test_same_types(self):
        """
        Test that a Pokemon with the same type twice is monotype.
        """
        Fireflame = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Fire', 'Fire', 'Special')

        FireflameString = 'Fire [Fire] [175/120/120/120/120/120] <Special>'

        self.assertEqual(FireflameString, str(Fireflame))

    def test_equality(self):
        """
        Test that Pokemon equality works as intended
        """

        pokemon_one = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire')
        clone = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire')
        pokemon_two = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Ice')

        self.assertEqual(pokemon_one, pokemon_one)
        self.assertEqual(pokemon_one, clone)
        self.assertNotEqual(pokemon_one, pokemon_two)
        self.assertNotEqual(pokemon_one, "Pikachu")

class TestCalculateDamage(unittest.TestCase):
    """
    Test the damage calculator function and string function from the Pokemon library
    """

    def test_stab(self):
        """
        Test that a Pokemon with STAB does 1.5x damage
        """
        non_stab_attacker = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire')
        stab_attacker= pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', move_type = 'Fire')
        stab_attacker_secondary= pok.Pokemon(100, 100, 100, 100, 100, 100, 'Normal', 'Fire', move_type = 'Fire')
        defender = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Normal')

        self.assertEqual(pok.calculate_damage(non_stab_attacker, defender, use_random=False), 28)
        self.assertEqual(pok.calculate_damage(stab_attacker, defender, use_random=False), 42)
        self.assertEqual(pok.calculate_damage(stab_attacker_secondary, defender, use_random=False), 42)

    def test_type_effectiveness(self):
        """
        Test that a Pokemon with type matchups deals appropriate damage
        """
        attacker = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Ground', move_type = 'Ground')
        defender_neutral = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Normal')
        defender_super = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire')
        defender_super_duper = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Electric')
        defender_not_very = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Bug')
        defender_not_very_at_all = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Bug', 'Grass')
        defender_literally_none = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Flying')

        self.assertEqual(pok.calculate_damage(attacker, defender_neutral, use_random=False), 42)
        self.assertEqual(pok.calculate_damage(attacker, defender_super, use_random=False), 85)
        self.assertEqual(pok.calculate_damage(attacker, defender_super_duper, use_random=False), 170)
        self.assertEqual(pok.calculate_damage(attacker, defender_not_very, use_random=False), 21)
        self.assertEqual(pok.calculate_damage(attacker, defender_not_very_at_all, use_random=False), 10)
        self.assertEqual(pok.calculate_damage(attacker, defender_literally_none, use_random=False), 0)

    def test_physical_vs_special(self):
        """
        Test that a Pokemon using its preferred stat will do more damage
        """
        attacker_p = pok.Pokemon(100, 50, 100, 150, 100, 100, 'Electric', move_type = 'Electric', damage_category='Physical')
        attacker_s = pok.Pokemon(100, 50, 100, 150, 100, 100, 'Electric', move_type = 'Electric', damage_category='Special')
        attacker_na = pok.Pokemon(100, 50, 100, 150, 100, 100, 'Electric', move_type = 'Electric', damage_category='Status')
        defender = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Normal')

        self.assertEqual(pok.calculate_damage(attacker_p, defender, use_random=False), 26)
        self.assertEqual(pok.calculate_damage(attacker_s, defender, use_random=False), 59)
        try:
            self.assertEqual(pok.calculate_damage(attacker_na, defender, use_random=False), 0)
        except ValueError as err:
            pass

class TestBattlePokemon(unittest.TestCase):
    """
    Tests the Pokemon battle simluator function from the Pokemon library
    """

    def test_regular_battle(self):
        """
        Tests same Pokemon battling similar Pokemon. First attacker should win.
        """
        pok_1 = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Electric', move_type = 'Electric', damage_category='Physical')
        pok_2 = pok.Pokemon(100, 100, 100, 100, 100, 99, 'Electric', move_type = 'Electric', damage_category='Physical')

        self.assertEqual(pok.battle_pokemon(pok_1, pok_2, use_random=False), (pok_1, 9))
        self.assertEqual(pok.battle_pokemon(pok_2, pok_1, use_random=False), (pok_1, 9))

    def test_randomly_selected_battle(self):
        """
        Tests two Pokemon that cannot attack one another. Either can win, but should be on turn 0.
        """
        pok_1 = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Ghost', move_type = 'Ghost', damage_category='Physical')
        pok_2 = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Normal', move_type = 'Normal', damage_category='Physical')

        self.assertEqual(pok.battle_pokemon(pok_1, pok_2, use_random=False)[1], 0)
        self.assertEqual(pok.battle_pokemon(pok_2, pok_1, use_random=False)[1], 0)

    def test_one_sided_battle(self):
        """
        Tests two Pokemon where only one can hurt the other. Second attacker should win.
        """
        pok_1 = pok.Pokemon(100, 100, 100, 100, 50, 100, 'Electric', move_type = 'Electric', damage_category='Physical')
        pok_2 = pok.Pokemon(100, 100, 100, 100, 100, 50, 'Ground', move_type = 'Ground', damage_category='Special')

        self.assertEqual(pok.battle_pokemon(pok_1, pok_2), (pok_2, 2))
        self.assertEqual(pok.battle_pokemon(pok_2, pok_1), (pok_2, 2))

class BreedPokemon(unittest.TestCase):
    """
    Tests the Pokemon breeding function from the Pokemon library
    """

    def test_breed(self):
        """
        Tests breeding regular Pokemon regularly
        """
        father = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Ice', 'Dark', 'Physical')
        mother = pok.Pokemon(75, 75, 75, 75, 75, 75, 'Water', 'Fire', 'Grass', 'Special')
        child = pok.breed_pokemon(father, mother)

        self.assertTrue(child.base_hp == 100 or child.base_hp == 75)
        self.assertTrue(child.base_attack == 100 or child.base_attack == 75)
        self.assertTrue(child.base_defense == 100 or child.base_defense == 75)
        self.assertTrue(child.base_special_attack == 100 or child.base_special_attack == 75)
        self.assertTrue(child.base_special_defense == 100 or child.base_special_defense == 75)
        self.assertTrue(child.base_speed == 100 or child.base_speed == 75)
        self.assertTrue(child.type_primary == 'Fire' or child.type_primary == 'Water')
        self.assertTrue(child.type_secondary == 'Ice' or child.type_secondary == 'Fire' or child.type_secondary is None)
        self.assertTrue(child.move_type == 'Dark' or child.move_type == 'Grass')
        self.assertTrue(child.damage_category == 'Physical' or child.damage_category == 'Special')

class MutatePokemon(unittest.TestCase):
    """
    Tests the Pokemon mutation function from the Pokemon library
    """

    def test_mutate_once(self):
        """
        Tests that a new Pokemon is created
        """
        pokemon_one = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fake', 'Fake', 'Fake', 'Physical')
        pokemon_two = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fake', 'Fake', 'Fake', 'Physical')
        self.assertEqual(pokemon_one, pokemon_two)
        pokemon_two.mutate()
        self.assertNotEqual(pokemon_one, pokemon_two)

    def test_mutate_types(self):
        """
        Tests that each non-stat mutation functions as expected
        """
        pokemon = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fake', 'Bird', 'Fake', 'Physical')
        self.assertEqual(pokemon.type_primary, 'Fake')
        pokemon.mutate('Primary Type')
        self.assertNotEqual(pokemon.type_primary, 'Fake')
        self.assertEqual(pokemon.type_secondary, 'Bird')
        pokemon.mutate('Secondary Type')
        self.assertNotEqual(pokemon.type_secondary, 'Bird')
        self.assertEqual(pokemon.move_type, 'Fake')
        pokemon.mutate('Move Type')
        self.assertNotEqual(pokemon.move_type, 'Fake')
        self.assertEqual(pokemon.damage_category, 'Physical')
        pokemon.mutate('Damage Category')
        self.assertEqual(pokemon.damage_category, 'Special')
        pokemon.mutate('Damage Category')
        self.assertEqual(pokemon.damage_category, 'Physical')


if __name__ == '__main__':
    unittest.main()
