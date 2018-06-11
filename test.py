import sys
import matplotlib.pyplot as plt
import numpy as np

from creature import Creature as cr
import creature as creature_file

def breed_linear(gen0, num_generations):
    current_breeders = gen0[:]
    all_creatures = [gen0]
    for generation_idx in range(1, num_generations):
        new_cr_1 = current_breeders[0].breed_with(current_breeders[1])
        new_cr_2 = current_breeders[0].breed_with(current_breeders[1])

        current_breeders = [new_cr_1, new_cr_2]
        all_creatures.append(current_breeders)

    return all_creatures

dummy_ideals_buffalo = {
    'composed' : 10,
    'nurturing' : 3,
    'loyal' : 10,
    'fur' : 5,
    'fat' : 5
}

def calculate_dummy_fitness(creature):
    creature_abilities, debilities = creature.sum_gene_attributes()
    fitness = 0
    all_abilities = creature_file.psyche[:]
    all_abilities += creature_file.tissue
    all_abilities += creature_file.morphology

    for ability in all_abilities:
        if ability in creature_abilities:
            if ability in dummy_ideals_buffalo:
                fitness -= abs(dummy_ideals_buffalo[ability] - creature_abilities[ability])
            else:
                fitness -= creature_abilities[ability]
        elif ability in dummy_ideals_buffalo:
            fitness -= dummy_ideals_buffalo[ability]

    return fitness


def breed_dummy_fitness(gen0, num_generations):
    all_creatures = [gen0]
    current_breeders = gen0[:]
    num_creatures_in_gen = 6

    for generation_idx in range(1, num_generations):

        #Breed some creatures, add all to the set of creatures
        #Evaluate "fitness" for each creature

        all_creatures.append([])
        generation_fitness = []
        for creature_idx in range(num_creatures_in_gen):
            curr_creature = current_breeders[0].breed_with(current_breeders[1])
            curr_fitness = calculate_dummy_fitness(curr_creature)

            all_creatures[generation_idx].append(curr_creature)
            generation_fitness.append([creature_idx, curr_fitness])

        #Set current_breeders to the two most fit creatures
        generation_fitness = sorted(generation_fitness, key = lambda x : x[1],
            reverse = True)
        current_breeders[0] = all_creatures[generation_idx][generation_fitness[0][0]]

        current_breeders[1] = all_creatures[generation_idx][generation_fitness[1][0]]

    return all_creatures

breeding_schemes = {'linear_scheme' : breed_linear, "fitness" : breed_dummy_fitness}

def print_results(species, num_generations, creatures, print_all_gens = False):
    if (print_all_gens):
        for generation_idx in range(num_generations):
            print('Creatures in generation ' + str(generation_idx) + ':')
            n = 1
            for creature in creatures[generation_idx]:
                #print('Genetic material: ')
                #for creature_chromosome, genes in creature.chromosomes.items():
                    #print(creature_chromosome)
                    #for gene in genes:
                        #print(gene)
                print('Sum of genetic attributes, creature ' + str(n) + ': ')
                print(creature.sum_gene_attributes())
                print('Creature fitness: ' + str(calculate_dummy_fitness(creature)))
                print()
                n += 1
            print()
    else:
        print('Creatures in the final generation:')
        n = 1
        for creature in creatures[-1]:
            print('Sum of genetic attributes, creature ' + str(n) + ':')
            print(creature.sum_gene_attributes())
            print('Creature fitness: ' + str(calculate_dummy_fitness(creature)))
            print()
            n += 1

def plot_fitness(num_generations, creatures):
    ave_fitness = [0] * num_generations
    for generation_idx in range(num_generations):
        generation_fitness = []
        for creature in creatures[generation_idx]:
            generation_fitness.append(calculate_dummy_fitness(creature))
        ave_fitness[generation_idx] = np.mean(generation_fitness)
    plt.plot(ave_fitness)
    plt.show()

def main(num_generations = 5, species = 'buffalo', breeding_scheme = 'linear_scheme'):
    creature_1 = cr.new_creature(species)
    creature_2 = cr.new_creature(species)

    gen0 = [creature_1, creature_2]

    result = breeding_schemes[breeding_scheme](gen0, num_generations)

    print_results(species, num_generations, result)
    plot_fitness(num_generations, result)
    exit()

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) >= 1:
        num_generations = int(args[0])
    else:
        main()
    if len(args) >= 2:
        species = args[1]
    else:
        main(num_generations)
    if len(args) >= 3:
        breeding_scheme = args[2]
    else:
        main(num_generations, species)
    main(num_generations, species, breeding_scheme)
