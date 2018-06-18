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
        creatures = run_main_loop(creatures)
        max_fur = 0
        max_i = 0
        for i in range(num_keepable_creatures):
            if creatures[i].sum_gene_attributes()[0]['fur'] > max_fur:
                max_fur = creatures[i].sum_gene_attributes()[0]['fur']
                max_i = i
            if max_fur > 5:
                print()
                print()
                print("Congratulations, you have a very wooly buffalo")
                print()
                print("You won the game with a buffalo with the following stats:")
                print(str(max_i) + ": "+ str(creatures[max_i].sum_gene_attributes()[0]))
                exit()



def run_main_loop(creatures):
    creatures_temp = [] * num_keepable_creatures
    print("These are your current buffalos:")
    print()

    for i in range(num_keepable_creatures):
        print(str(i) + ": "+ str(creatures[i].sum_gene_attributes()[0]))
        print()

    print("Select 2 pairs to breed, each providing 3 buffalos for the next generation")


    pair1first = int(input("Select first partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
    print("You selected " + str(pair1first))

    pair1second = int(input("Select second partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
    print("You selected " + str(pair1second))

    while pair1first == pair1second:
        print("It cannot breed with itself, please select another")
        pair1second = int(input("Select second partner in first pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
        print("You selected " + str(pair1second))

    pair2first = int(input("Select first partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
    print("You selected " + str(pair2first))

    pair2second = int(input("Select second partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
    print("You selected " + str(pair2second))

    while pair2first == pair2second:
        print("It cannot breed with itself, please select another")
        pair2second = int(input("Select second partner in second pair (a number 0 - " + str(num_keepable_creatures - 1) + "): ", ))
        print("You selected " + str(pair2second))

    print()
    for i in range(num_keepable_creatures):
        if i < num_keepable_creatures/2:
            cre = creatures[pair1first].breed_with(creatures[pair1second])
        else:
            cre = creatures[pair2first].breed_with(creatures[pair2second])
        if cre == None:
            print("Breed failed. Handling of this state is not implemented. Shuting down")
            exit()
        creatures_temp.append(cre)
    return creatures_temp


if __name__ == '__main__':
    main()
