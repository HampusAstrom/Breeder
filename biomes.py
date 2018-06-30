# import Creature from creature.py as creatures

forest_ranges = {
    'cold_resist' : ['lower', -2],
    'heat_resist' : ['lower', -2],
    'energy_need' : ['upper', 30],
    'tree_climber' : ['lower', -4]
}

desert_ranges = {
    'cold_resist' : ['lower', -2],
    'heat_resist' : ['lower', 3],
    'energy_need' : ['upper', 25],
    'foraging' : ['lower', 2]
}

tundra_ranges = {
    'cold_resist' : ['lower', 3],
    'energy_need' : ['upper', 25],
    'foraging' : ['lower', 2]
}

savannah_ranges = {
    'heat_resist' : ['lower', 3],
    'energy_need' : ['upper', 30]
}

mountain_ranges = {
    'cold_resist' : ['lower', 2],
    'energy_need' : ['upper', 25],
    'foraging' : ['lower', 2]
}

domestic_ranges = {
    'tame' : ['lower', 5],
    'intelligent' : ['lower', 2],
    'intelligent' : ['upper', 8],
    'social' : ['lower', 5]
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
        for ab, limit in self._ab_ranges.items():
            if limit[0] == 'lower':
                if limit[1] <= creature_abilities[ab]:
                    fitness += inc
                else:
                    fitness -= inc
            else:
                if limit[1] >= creature_abilities[ab]:
                    fitness += inc
                else:
                    fitness -= inc

        return fitness

    def get_name(self):
        return _name
