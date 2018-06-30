import Creature from creature.py as creatures

forest_ranges = {
    'cold_resist' : [0, 5],
    'heat_resist' : [0, 5],
    'energy_need' : [0, 50],
    'tree_climber' : [3, 50]
}

desert_ranges = {
    'cold_resist' : [0, 5],
    'heat_resist' : [5, 10],
    'energy_need' : [0, 20],
    'foraging' : [5, 10]
}

tundra_ranges = {
    'cold_resist' : [5, 10],
    'energy_need' : [0, 20],
    'foraging' : [5, 10]
}

savannah_ranges = {
    'heat_resist' : [3, 10],
    'energy_need' : [0, 50]
}

mountain_ranges = {
    'cold_resist' : [3, 10],
    'energy_need' : [0, 15],
    'foraging' : [5, 10]
}

domestic_ranges = {
    'tame' : [5, 100],
    'intelligent' : [3, 8],
    'social' : [10, 20]
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
        self._ab_ranges = der_ab_ranges[_type]

    def get_type(self):
        return _type

    def check_fitness(self, creature_abilities):
        fitness = 0
        inc = 10/len(self._ranges)
        for ab, span in self._ab_ranges.items():
            if span[0] < creature_abilities[ab] and span[1] > creature_abilities[ab]:
                fitness += inc
            else:
                fitness -= inc
        return fitness

    def get_name(self):
        return _name
