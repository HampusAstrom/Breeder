import numpy as np
import random as rng
import math


# All creatures have the 3 base chromosomes
# special creatures might have additional chromosomes for special abilities

# each chromosome contains two lists of gene slots (default 20 slots per list)
# ability genes, that are usually what you want
# debility genes, that only hurts when the same is present many times in a
# chromosome (gets exponentially worse, after first 2-3?)

# derived abilities
# cold resistance
# heat resistance
# energy needs
# water needs?
# endurance
# strength
#
# domesticated (might depend on other mental attributes)
# social
# obedient
# brave
# violent
# terrifying
# intelligent/smart
# protective (might depend on other mental attributes)
# perceptive
# independent/loner


# default breeding genre recombination scheme
# for each gene slot in offspring:
#   randomly select one parent and take its gene with the same slot index
#   (a gene is a ability/debility pair)
#
# possible mutations versions:
#   the ability or debility part of a gene in the offspring gets a random value
#   rather than the value of its parent, the other part is still the same
#       - should be rare but important
#
#   the gene is taken from one of the parents from gene index +-1 instead of same
#       - probably most common change
#
#   the possition of two (consecutive) genes is swaped after they are
#   determined as normal
#       - could probably be fairly common, similar effect to previous method
#
#   one gene is added or removed, shifting all the following gene possitions
#       - probably way too big a change in later generation, dont use!
#
#

# Ideas for base chromosomes and their genes
# psyche chromosome:
psyche = [
    'composed',
    'energetic',
    'aggressive',
    'creative',
    'nurturing',
    'manipulative',
    'feral',
    'loyal',
    'autonomous',
    'attentive'
]
#
# tissue chromosome:
tissue = [
    'fur',
    'scales',
    'sweat_glands',
    'fat',
    'slow_muscles',
    'fast_muscles',
    'lightweight_bones'
]

# morphology chromosome:
morphology = [
    'hearing',
    'frontlimb focus',
    'backlimb focus',
    'vision',
    'jaw_focus',
    'fine_motorics', #?
    'claws',
    'horns',        #or tusks?
    'fangs',
    'poison_glands',
    'winged_frontlimbs',
    'venom_glands',
    'smell',
    'antennae',     #?
    'big_brain',    #?
    'herbivore'     # (grass/leaves)
]

base_chromosomes = {
    'morphology' : morphology,
    'tissue': tissue,
    'psyche': psyche
}

#
# to add: small with many kids? vs large with fewer kids?

chromosome_length = 20
debilities_per_cromosome = chromosome_length

# It's possible that there should be some modifications to the various loci in
# the species dictionary, somehow

species_list = {
    'buffalo': {
        'psyche': {
            'neutral': 10,
            'composed': 1,
            'nurturing': 1,
            'loyal': 1,
            'feral': 2
        },
        'tissue': {
            'neutral': 10,
            'fur': 2,
            'slow_muscles': 2,
            'fat': 1
        },
        'morphology': {
            'neutral': 9,
            'jaw_focus': 1,
            'smell': 1,
            'herbivore': 2,
            'horns' : 2,
        },
    }
}

class Creature:
    # should only be used by internal functions
    # _init_from_species and _init_from_parents
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes;

    # returns a new creature
    @classmethod
    def _init_from_species(cls, species):
        if not species in species_list:
            print("Species not listed, cannot create")
            return None

        model_species = species_list[species]
        chromosomes = {}
        for chromosome, species_genes_full in model_species.items():
            loci_width = math.floor(chromosome_length/len(base_chromosomes[chromosome]))
            curr_chromosome = [(0,0)] * chromosome_length
            weight_neutral = species_genes_full['neutral']
            species_genes = species_genes_full.copy()
            del species_genes['neutral']

            loci = range(0, chromosome_length, loci_width)
            total_present = sum(species_genes.values())
            total = total_present + weight_neutral
            nnz = math.floor(rng.gauss(total_present, total/8) * chromosome_length/total)
            nnz = min(nnz, chromosome_length)

            non_neutral_genes = rng.choices(list(species_genes.keys()), weights = species_genes.values(), k = nnz)

            for idx_nz_gene in range(nnz):
                displacement = math.floor(rng.gauss(loci_width/2, loci_width/4))

                # create the debilities as well here; for now they will all be zero.
                gene_position_idx = base_chromosomes[chromosome].index(non_neutral_genes[idx_nz_gene])
                gene_position = (loci[gene_position_idx] + displacement)%(chromosome_length-1)
                ability_value = base_chromosomes[chromosome].index(non_neutral_genes[idx_nz_gene])+1
                debility_value = rng.randint(1,debilities_per_cromosome)
                gene_value = (ability_value, debility_value)

                if curr_chromosome[gene_position][0] is not 0:
                    curr_chromosome[gene_position] = gene_value

                else:
                    slip_dir = rng.choice((-1,1))
                    slips = 1
                    while(curr_chromosome[gene_position + slip_dir*slips])[0] is not 0:
                        slips = slips + 1
                        if gene_position + slip_dir * slips >= chromosome_length:
                            gene_position = gene_position - chromosome_length
                    curr_chromosome[gene_position + slip_dir * slips] = gene_value

            chromosomes[chromosome] = curr_chromosome
        return cls(chromosomes)

    # returns a new creature as offspring
    @classmethod
    def _init_from_parents(cls, parent1, parent2):
        combined_chromosomes = []
        chromosomes = {}

        for chrome, genes in parent1.chromosomes.items():
            if chrome in parent2.chromosomes:
                combined_chromosomes.append(chrome)
            elif rng.randint(0,1) is 1:
                chromosomes[chrome] = genes

        for chrome, genes in parent2.chromosomes.items():
            if chrome not in parent1.chromosomes:
                if rng.randint(0,1) is 1:
                    chromosomes[chrome] = genes

        for chrome in combined_chromosomes:
            curr_chromosome = [(0,0)] * chromosome_length
            for i in range(len(curr_chromosome)):
                if rng.randint(0,1) is 1:
                    curr_chromosome[i] = parent1.chromosomes[chrome][i]
                else:
                    curr_chromosome[i] = parent2.chromosomes[chrome][i]
            chromosomes[chrome] = curr_chromosome

        return cls(chromosomes)

    @classmethod
    def new_creature(cls, species):
        return cls._init_from_species(species)

    def breed_with(self, partner):
        # check if they match enough to breed
        if (not self.match_with(partner)):
            return None

        # create offspring
        return self._init_from_parents(parent1=self, parent2=partner)

    def match_with(self, partner):
        if partner is self:
            return False
        return True

    # returns a dictionary of the chromosomes with sums for all present attributes
    def sum_gene_attributes(self):
        ab = {}
        deb = {}
        for chrome, genes in self.chromosomes.items():
            for gene in genes:
                if gene[0] is not 0:
                    ability = base_chromosomes[chrome][gene[0]-1]
                    if ability in ab:
                        ab[ability] += 1
                    else:
                        ab[ability] = 1
                if gene[1] is not 0:
                    debility = chrome + str(gene[1])
                    if debility in deb:
                        deb[debility] += 1
                    else:
                        deb[debility] = 1
        return ab, deb
