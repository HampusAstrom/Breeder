from contextlib import redirect_stdout
from io import StringIO
import unittest
import creature as cr
import biomes as bi
from get_wool_dont_overheat import Shop

# typical example chromosome and resulting attributes
CROME1 = {'psyche': [(0, 0), (1, 17), (1, 10), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 19), (0, 0), (0, 0), (0, 0), (0, 0), (7, 16), (7, 18), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
          'tissue': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 10), (0, 0), (0, 0), (0, 0), (5, 12), (5, 14), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 18)],
          'morphology': [(0, 0), (0, 0), (0, 0), (5, 10),(0, 0), (0, 0), (8, 14), (0, 0), (0, 0), (0, 0), (0, 0), (13, 17), (0, 0), (13,3), (16, 12), (0, 0), (16, 13), (16, 8), (16, 11), (0,0)]}
GENEATTRI1 = ({'composed': 2, 'nurturing': 1, 'feral': 2, 'fat': 1, 'slow_muscles': 2, 'fur': 1, 'jaw_focus': 1, 'horns': 1, 'smell': 2, 'herbivore': 4}, {'psyche17': 1, 'psyche10': 1, 'psyche19': 1, 'psyche16': 1, 'psyche18': 1, 'tissue10': 1, 'tissue12': 1, 'tissue14': 1, 'tissue18': 1, 'morphology10': 1, 'morphology14': 1, 'morphology17': 1, 'morphology3': 1, 'morphology12': 1, 'morphology13': 1, 'morphology8': 1, 'morphology11': 1})
DERIVATTRI1 = {'cold_resist': 2, 'heat_resist': -2, 'energy_need': 17, 'hunt_chase': 0.0, 'hunt_ambush': 2.0, 'camouflage': 2, 'flee': 1, 'violent': 5, 'social': -1.0, 'brave': 4, 'eat_resist': 0, 'tree_climber': -1, 'tame': -8, 'foraging': 2, 'intelligent': 0}

    # another typical chromosome and resulting attributes, used to check recombination
CROME2 = {'psyche': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1), (5, 17), (0, 0), (0, 0), (0, 0), (7, 3), (0, 0), (8, 7), (0, 0), (8, 16), (0, 0), (0, 0), (0, 0)],
          'tissue': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 13), (0, 0), (0, 0), (0, 0), (0, 0), (5, 9), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
          'morphology': [(0, 0), (0, 0), (0, 0), (5, 1), (0, 0), (5, 3), (0, 0), (0, 0), (8, 2), (0, 0), (0, 0), (0, 0), (13, 10), (16, 15), (16, 12), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]}
GENEATTRI2 = ({'nurturing': 1, 'feral': 1, 'loyal': 2, 'fat': 1, 'slow_muscles': 1, 'jaw_focus': 2, 'horns': 1, 'smell': 1, 'herbivore': 2}, {'psyche1': 1, 'psyche17': 1, 'psyche3': 1, 'psyche7': 1, 'psyche16': 1, 'tissue13': 1, 'tissue9': 1, 'morphology1': 1, 'morphology3': 1, 'morphology2': 1, 'morphology10': 1, 'morphology15': 1, 'morphology12': 1})
DERIVATTRI2 = {'cold_resist': 1, 'heat_resist': -1, 'energy_need': 12, 'hunt_chase': 0.0, 'hunt_ambush': 0.0, 'camouflage': -1, 'flee': 0, 'violent': 4, 'social': 2.0, 'brave': 1, 'eat_resist': 0, 'tree_climber': -1, 'tame': -3, 'foraging': 1, 'intelligent': -2}
class TestCreature(unittest.TestCase):

    def test_init_from_species(self):
        # Create an animal that exists in the list
        buff1 = cr.Creature.new_creature('buffalo')
        self.assertIsNotNone(buff1)

        # Create an animal that does not exists in the list
        with redirect_stdout(StringIO()) as stdout:
            wrong = cr.Creature.new_creature('asdasdssdffal')
            self.assertIsNone(wrong)
        self.assertEqual(stdout.getvalue(), "Species not listed, cannot create\n")

    # Test when breeding is viable
    def test_breedning_match(self):
        buff1 = cr.Creature.new_creature('buffalo')
        buff2 = cr.Creature.new_creature('buffalo')

        # You cannot breed with yourself
        self.assertFalse(buff1.match_with(buff1))
        self.assertEqual(buff1.breed_with(buff1), None)

        # You can breed with another member of your species
        self.assertTrue(buff1.match_with(buff2))
        self.assertIsNotNone(buff1.breed_with(buff2))

    # Test breeding results
    def test_breedning(self):
        buff1 = cr.Creature.new_creature('buffalo')
        buff2 = cr.Creature.new_creature('buffalo')

        def test_identical(self):
            # Animals with identical chromosomes bred should procude children with
            # chromosomres identical to their parents, if random mutations are turned off
            buff1.chromosomes = CROME1
            buff2.chromosomes = CROME1
            child = buff1.breed_with(buff2)
            self.assertEqual(child.chromosomes, CROME1)

        def test_different(self):
            # Animals with diffrent chromosomes bred should produce children where each
            # gene is either of their parents genes, if random mutations are turned off
            buff1.chromosomes = CROME1
            buff2.chromosomes = CROME2
            child = buff1.breed_with(buff2)
            for key, value in child.chromosomes.items():
                for g, gene in enumerate(value):
                    with self.subTest(chomosome=key, gene=g):
                        self.assertTrue(gene == buff1.chromosomes[key][g] or gene == buff2.chromosomes[key][g])

        # Test breeding without chunking
        cr.set_rand_mutate_chance(0)
        cr.set_use_chunk_combining(False)
        with self.subTest(chunking=False):
            test_identical(self)
            test_different(self)

        # Test breeding with chunking (with chunk_shift_chance of 0 as it is random)
        cr.set_rand_mutate_chance(0)
        cr.set_use_chunk_combining(True)
        cr.set_chunk_shift_chance(0)
        with self.subTest(chunking=True):
            test_identical(self)
            test_different(self)

    # I am not sure this test is good, as derived abilities equations could change
    # Test that abilities are derived correctly
    def test_derived_abilities(self):
        buff1 = cr.Creature.new_creature('buffalo')

        buff1.chromosomes = CROME1
        derived_abs1 = buff1.evaluate_derived_abilities()
        self.assertEqual(derived_abs1, DERIVATTRI1)

    # Test that gene attributes are summed correctly
    def test_gene_attributes(self):
        buff1 = cr.Creature.new_creature('buffalo')

        buff1.chromosomes = CROME1
        gene_abs1 = buff1.sum_gene_attributes()
        self.assertEqual(gene_abs1, GENEATTRI1)


class TestBiomes(unittest.TestCase):
    def test_init_biome(self):
        # Create an biome that exists in the list
        biome = bi.Biome.init_biome('test_tundra', 'tundra')
        self.assertIsNotNone(biome)

        # Create an biome that does not exists in the list
        with redirect_stdout(StringIO()) as stdout:
            wrong = bi.Biome.init_biome('test_wrong', 'saasdfasdaetafdas')
            self.assertIsNone(wrong)
        self.assertEqual(stdout.getvalue(), 'Unknown biome, cannot create\n')

    def test_check_fitness(self):
        biome = bi.Biome.init_biome('test_tundra', 'tundra')
        buff1 = cr.Creature.new_creature('buffalo')
        buff1.chromosomes = CROME1
        derived_abs1 = buff1.evaluate_derived_abilities()
        self.assertEqual(biome.check_fitness(derived_abs1), 3.3333333333333335)

class TestShop(unittest.TestCase):
    def test_init(self):
        # create with working list of species
        shop = Shop(5, ['buffalo'])
        self.assertEqual(len(shop.stocks), 5)
        self.assertEqual(shop.stocks[0][0], 'buffalo')

        # create with falty list of species
        with redirect_stdout(StringIO()) as stdout:
            with self.assertRaises(SystemExit) as e:
                shop = Shop(5, ['asdfasdasd'])
        self.assertEqual(stdout.getvalue(), "Species not listed, cannot create\nFailed to create shop creatures. Shuting down.\n")

if __name__ == '__main__':
    unittest.main()
