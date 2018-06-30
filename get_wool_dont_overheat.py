import sys
import matplotlib.pyplot as plt
import numpy as np
import random as rng

import creature as cr

num_keepable_creatures = 6

def main():

    creatures = [] * num_keepable_creatures
    for i in range(num_keepable_creatures):
        c = cr.Creature.new_creature('buffalo')
        if c != None:
            creatures.append(c)
        else:
            print("Failed to create inital creatures. Shuting down.")
            exit()

    print("Welcome to creature breeder")
    print("Try to breed wooly and manageble buffalos without letting them overheat")
    print()

    turn_counter = 0

    while True:
        turn_counter += 1
        print()
        print("TURN " + str(turn_counter))
        print()

        if turn_counter % 5 == 0:
            creatures = go_to_shop(creatures)

        creatures = decide_breeding(creatures)
        max_fur = 0
        max_i = 0
        for i in range(num_keepable_creatures):
            if 'fur' in creatures[i].sum_gene_attributes()[0]:
                if creatures[i].sum_gene_attributes()[0]['fur'] > max_fur:
                    max_fur = creatures[i].sum_gene_attributes()[0]['fur']
                    max_i = i
            derived = creatures[i].evaluate_derived_abilities()
            #heat = 0
            #if 'fur' in creatures[i].sum_gene_attributes()[0]:
            #    heat += creatures[i].sum_gene_attributes()[0]['fur']
            #if 'fat' in creatures[i].sum_gene_attributes()[0]:
            #    heat += creatures[i].sum_gene_attributes()[0]['fat']
            if derived['heat_resist'] == -7:
                print("WARNING! Buffalo " + str(i) + " gets really hot in the summer, if it gets worse you will lose.")
            if derived['heat_resist'] < -7:
                print("Buffalo " + str(i) + " got too hot this summer and died, you loose.")
                exit()
            if derived['violent'] > 13:
                print("Buffalo " + str(i) + " whent berserk this summer and killed you, you loose.")
                exit()
            if derived['violent'] > 11:
                print("WARNING! Buffalo " + str(i) + " is very violent, if it gets worse you will lose.")


        derived = creatures[max_i].evaluate_derived_abilities()
        if max_fur > 5 and derived['violent'] > 5:
            print()
            print("Buffalo " + str(max_i) + " is very wooly, but it is still wild and dangerous.")
            print("You need to make it easier to handle in order to have the perfect buffalo and win the game.")

        if max_fur > 5 and derived['violent'] <= 5:
            print()
            print()
            print("Congratulations, you have a very wooly and managable buffalo")
            print()
            print("You won the game on turn " + str(turn_counter) + " with a buffalo with the following stats:")
            print(str(max_i) + ": "+ str(creatures[max_i].sum_gene_attributes()[0]))
            exit()


def list_buffalos(creatures):
    for i in range(len(creatures)):
        print(str(i) + ": "+ str(creatures[i].sum_gene_attributes()[0]))
        print()

def go_to_shop(creatures):
    shop = Shop(2, ['buffalo'])
    print("There is a market this year. If you sell one buffalo you can buy a new buffalo")
    print("These are your current buffalos:")
    print()
    list_buffalos(creatures)
    while True:
        resp = input("Do you want to sell one of your buffalos (y/n)?")
        if resp == "y":
            slot = input("Which buffalo do you want to sell (a number 0 - " + str(num_keepable_creatures - 1) + ")?")
            print("You sold buffalo " + slot + ". Now you get to buy a buffalo.")
            print("These are the available buffalos:")
            print()
            list = shop.list_stocks_without_species_name()
            list_buffalos(list)
            bought = input("Which buffalo do you want to buy (a number 0 - " + str(len(list)-1) + ")?")
            creatures[int(slot)] = list[int(bought)]
            print("You bought buffalo " + bought + ". It is now your buffalo number " + slot + ". ")
            print()
            return creatures
        elif resp == "n":
            print("You deside not to trade on the market this year")
            print()
            return creatures
        else:
            print()
            print("You need to decide weither to trade or not. Type y or n")
            print()

def decide_breeding(creatures):
    creatures_temp = [] * num_keepable_creatures
    print("These are your current buffalos:")
    print()
    list_buffalos(creatures)

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


class Shop:
    def __init__(self, stock_size, avail_spec_list):
        self.stocks = []
        for i in range(stock_size):
            j = rng.randint(0,len(avail_spec_list)-1)
            c = cr.Creature.new_creature(avail_spec_list[j])
            if c != None:
                self.stocks.append((avail_spec_list[j], c))
            else:
                print("Failed to create shop creatures. Shuting down.")
                exit()

    def list_stocks_without_species_name(self):
        ret = []
        for i in range(len(self.stocks)):
            ret.append(self.stocks[i][1])
        return ret

if __name__ == '__main__':
    main()
