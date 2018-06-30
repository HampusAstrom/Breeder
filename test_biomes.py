import sys
import numpy as np

from creature import Creature
from biomes import Biome

def main():
    serengeti = Biome.init_biome('serengetti', 'savannah')
    siberia = Biome.init_biome('siberia', 'tundra')

    buff1 = Creature.new_creature('buffalo')
    buff2 = Creature.new_creature('buffalo')

    derived_abs1 = buff1.evaluate_derived_abilities()
    derived_abs2 = buff2.evaluate_derived_abilities()

    print('Buffalo 1 has a fitness value of ' + str(serengeti.check_fitness(derived_abs1))
        + ' in Serengeti and ' + str(siberia.check_fitness(derived_abs1)) + ' in Siberia.\n')
    print('Their base abilities are ' + str(buff1.sum_gene_attributes()[0]))
    print('Their derived abilities are ' + str(buff1.evaluate_derived_abilities()))
    print()
    print('Buffalo 2 has a fitness value of ' + str(serengeti.check_fitness(derived_abs2))
        + ' in Serengeti and ' + str(siberia.check_fitness(derived_abs2)) + ' in Siberia.\n')
    print('Their abilities are ' + str(buff2.sum_gene_attributes()[0]))
    print('Their derived abilities are ' + str(buff2.evaluate_derived_abilities()))


if __name__ == '__main__':
    main()
