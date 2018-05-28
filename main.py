import creature as cr

def main():
    buff = cr.Creature.new_creature('buffalo')
    buff2 = cr.Creature.new_creature('mouse')
    print(buff.chromosomes)
    print()
    print(buff.sum_gene_attributes())


if __name__ == '__main__':
    main()
