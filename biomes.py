# import Creature from creature.py as creatures

forest_ranges = {
    'cold_resist' : [-2, 50],
    'heat_resist' : [-2, 50],
    'energy_need' : [0, 50],
    'tree_climber' : [-4, 50]
}

desert_ranges = {
    'cold_resist' : [-2, 50],
    'heat_resist' : [3, 50],
    'energy_need' : [0, 25],
    'foraging' : [2, 50]
}

tundra_ranges = {
    'cold_resist' : [3, 50],
    'energy_need' : [0, 25],
    'foraging' : [2, 50]
}

savannah_ranges = {
    'heat_resist' : [3, 50],
    'energy_need' : [0, 50]
}

mountain_ranges = {
    'cold_resist' : [2, 50],
    'energy_need' : [0, 25],
    'foraging' : [2, 50]
}

domestic_ranges = {
    'tame' : [5, 100],
    'intelligent' : [2, 8],
    'social' : [5, 20]
}

der_ab_ranges = {
    'forest' : forest_ranges,
    'desert' : desert_ranges,
    'tundra' : tundra_ranges,
    'savannah' : savannah_ranges,
    'mountain' : mountain_ranges,
    'domestic' : domestic_ranges
}

class Biome:

    @classmethod
    def init_biome(cls, name, type):
        if type not in der_ab_ranges.keys():
            print('Unknown biome, cannot create')
            return None
        return cls(name, type)

    def __init__(self, name, type):
        self._region_name = name
        self._type = type
        self._ab_ranges = der_ab_ranges[self._type]

    def get_type(self):
        return _type

    def check_fitness(self, creature_abilities):
        fitness = 0
        inc = 10/len(self._ab_ranges)
        for ab, span in self._ab_ranges.items():
            if span[0] < creature_abilities[ab] and span[1] > creature_abilities[ab]:
                fitness += inc
            else:
                fitness -= inc
        return fitness

    def get_name(self):
        return _name
