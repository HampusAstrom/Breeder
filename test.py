import sys

from creature import Creature as cr

def breed_linear(gen0, num_generations):
    current_breeders = gen0
    all_creatures = [gen0]
    for generation_idx in range(1, num_generations):
        new_cr_1 = current_breeders[0].breed_with(current_breeders[1])
        new_cr_2 = current_breeders[0].breed_with(current_breeders[1])

        current_breeders = [new_cr_1, new_cr_2]
        all_creatures.append(current_breeders)

    return all_creatures

breeding_schemes = {'linear_scheme' : breed_linear}

def print_results(species, num_generations, creatures):
    for generation_idx in range(num_generations):
        print('Creatures in generation ' + str(generation_idx) + ':')
        for creature in creatures[generation_idx]:
            print('Genetic material: ')
            for creature_chromosome, genes in creature.chromosomes.items():
                print(creature_chromosome)
                for gene in genes:
                    print(gene)
            print('Sum of genetic attributes: ')
            print(creature.sum_gene_attributes())
        print()

def main(num_generations = 5, species = 'buffalo', breeding_scheme = 'linear_scheme'):
    creature_1 = cr.new_creature(species)
    creature_2 = cr.new_creature(species)

    gen0 = [creature_1, creature_2]

    result = breeding_schemes[breeding_scheme](gen0, num_generations)

    print_results(species, num_generations, result)
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
