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
        self.assertEqual(Mew.hp, 100)
        self.assertEqual(Mew.attack, 100)
        self.assertEqual(Mew.defense, 100)
        self.assertEqual(Mew.special_attack, 100)
        self.assertEqual(Mew.special_defense, 100)
        self.assertEqual(Mew.speed, 100)
        self.assertEqual(Mew.type_primary, 'Psychic')
        self.assertEqual(Mew.type_secondary, None)
        self.assertEqual(Mew.move_type, 'Normal')
        self.assertEqual(Mew.damage_category, 'Physical')

        MewString = 'Psychic [Normal]'
        MewString += "\nHP: 100"
        MewString += "\nAtk: 100"
        MewString += "\nDef: 100"
        MewString += "\nSpA: 100"
        MewString += "\nSpD: 100"
        MewString += "\nSpd: 100"

        self.assertEqual(MewString, str(Mew))

    def test_all_fields(self):
        """
        Test that a Pokemon with all fields showing works as intended
        """
        Victini = pok.Pokemon(100, 100, 100, 100, 100, 100, 'Fire', 'Psychic', 'Fire', 'Special')
        self.assertEqual(Victini.hp, 100)
        self.assertEqual(Victini.attack, 100)
        self.assertEqual(Victini.defense, 100)
        self.assertEqual(Victini.special_attack, 100)
        self.assertEqual(Victini.special_defense, 100)
        self.assertEqual(Victini.speed, 100)
        self.assertEqual(Victini.type_primary, 'Fire')
        self.assertEqual(Victini.type_secondary, 'Psychic')
        self.assertEqual(Victini.move_type, 'Fire')
        self.assertEqual(Victini.damage_category, 'Special')

        VictiniString = 'Fire/Psychic [Fire]'
        VictiniString += "\nHP: 100"
        VictiniString += "\nAtk: 100"
        VictiniString += "\nDef: 100"
        VictiniString += "\nSpA: 100"
        VictiniString += "\nSpD: 100"
        VictiniString += "\nSpd: 100"

        self.assertEqual(VictiniString, str(Victini))

    def test_op(self):
        """
        Test that a Pokemon with over 600 stats works as intended
        """
        Strongo = pok.Pokemon(150, 150, 150, 150, 150, 40, 'Fighting')
        self.assertEqual(Strongo.hp, 113)
        self.assertEqual(Strongo.attack, 113)
        self.assertEqual(Strongo.defense, 113)
        self.assertEqual(Strongo.special_attack, 113)
        self.assertEqual(Strongo.special_defense, 113)
        self.assertEqual(Strongo.speed, 30)
        self.assertEqual(Strongo.type_primary, 'Fighting')
        self.assertEqual(Strongo.type_secondary, None)
        self.assertEqual(Strongo.move_type, 'Normal')
        self.assertEqual(Strongo.damage_category, 'Physical')

        StrongoString = 'Fighting [Normal]'
        StrongoString += "\nHP: 113"
        StrongoString += "\nAtk: 113"
        StrongoString += "\nDef: 113"
        StrongoString += "\nSpA: 113"
        StrongoString += "\nSpD: 113"
        StrongoString += "\nSpd: 30"

        self.assertEqual(StrongoString, str(Strongo))

if __name__ == '__main__':
    unittest.main()
