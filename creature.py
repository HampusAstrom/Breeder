import numpy as np
import random as rng


# All creatures have the 3 base chromosomes
# special creatures might have additional chromosomes for special abilities

# each chromosome contains two lists of gene slots (default 20 slots per list)
# ability genes, that are usually what you want
# debility genes, that only hurts when the same is present many times in a
# chromosome (gets exponentially worse, after first 2-3?)

# Ideas for base chromosomes and their genes
# psyche chromosome:
# ?: composed, aggressive, nurturing, creative, loyal, attentive, manipulative,
# autonomous, energetic, feral
#
# tissue chromosome:
# ?: fur, scales, sweat glands, fat, slow muscles, fast muscles,
# lightweight bones
#
# morphology chromosome:
# ?: claws, ears, venom glands, poison gland, winged frontlimbs, frontlimb focus,
# backlimb focus, fangs, jaw focus, fine motorics?, nose, eyes, antenna?,
# horns, herbivore (grass/leaves), big brain?
#
# to add: small with many kids? vs large with fewer kids?

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

species_list = {
    'buffalo': {
        'psyche': {
            'neutral': (10, None),
            'composed': 1,
            'nurturing': 1,
            'loyal': 1,
            'feral': 2
        },
        'tissue': {
            'neutral': (10, None),
            'fur': 2,
            'slow_muscles': 2,
            'fat': 1
        },
        'morphology': {
            'neutral': (10, None),
            'jaw_focus': 1,
            'nose': 1,
            'herbivore': 2
        },
    }
}

class Creature:
    # should only be used by internal functions
    # _init_from_species and _init_from_parents
    def __init__(self, kromosomes):
        self.kromosomes = kromosomes;

    # returns a new creature
    @classmethod
    def _init_from_species(cls, species):
        if species in species_list:
            return cls(1)
            #pass # TODO: implement kromosome creation here
            # return cls(kromosomes)
        else:
            print("Species not listed, cannot create")
            return None

    # returns a new creature as offspring
    @classmethod
    def _init_from_parents(cls, parent1, parent2):
        pass # TODO: implement kromosome creation here
        # return cls(kromosomes)

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
        return True
