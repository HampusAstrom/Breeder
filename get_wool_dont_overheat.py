import sys
import matplotlib.pyplot as plt
import numpy as np

import creature as cr

num_keepable_creatures = 6

def main():

    creatures = [] * num_keepable_creatures
    for i in range(num_keepable_creatures):
        creatures.append(cr.Creature.new_creature('buffalo'))

    print("Welcome to creature breeder")
    print("Try to breed wooly buffalos without letting them overheat")
    print()

    while True:
        run_main_loop(creatures)



def run_main_loop(creatures):
    print("These are your current buffalos:")
    print()

    for i in range(num_keepable_creatures):
        print(creatures[i].sum_gene_attributes())
        print()

    print("Select 2 pairs to breed, each providing 3 buffalos for the next generation")


    pair1first = input("Select first partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
    print("You selected " + str(pair1first))

    pair1second = input("Select second partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
    print("You selected " + str(pair1second))

    while pair1first == pair1second:
        print("It cannot breed with itself, please select another")
        pair1second = input("Select second partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
        print("You selected " + str(pair1second))

    pair2first = input("Select first partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
    print("You selected " + str(pair2first))

    pair2second = input("Select second partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
    print("You selected " + str(pair2second))

    while pair2first == pair2second:
        print("It cannot breed with itself, please select another")
        pair2second = input("Select second partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", )
        print("You selected " + str(pair2second))

    print()
    print("TODO: Breed")
    print()

if __name__ == '__main__':
    main()
