import creature as cr

def main():
    buff1 = cr.Creature.new_creature('buffalo')
    mouse = cr.Creature.new_creature('mouse')
    buff2 = cr.Creature.new_creature('buffalo')
    buff3 = cr.Creature.breed_with(buff1, buff2)
    print(buff1.chromosomes)
    print()
    print(buff2.chromosomes)
    print()
    print(buff3.chromosomes)
    print()
    print(buff1.sum_gene_attributes())
    print()
    print(buff2.sum_gene_attributes())
    print()
    print(buff3.sum_gene_attributes())
    print()


if __name__ == '__main__':
    main()
