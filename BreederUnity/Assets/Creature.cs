
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using static Util;
using UnityEngine;
using UnityEditor;

namespace Breeder
{

  public class Species
  {
    public string name;
    public List<(GeneDist dist, double weight)> geneList;

    public Species(string name)
    {
      this.name = name;
      this.geneList = new List<(GeneDist dist, double weight)>();
    }

    public void AddGeneDist(GeneDist geneDist, double weight)
    {
      geneList.Add((geneDist, weight));
    }

  }

  public class TraitDict : Dictionary<string, double>
  {

    public static TraitDict operator +(TraitDict d1, TraitDict d2)
    {
      TraitDict ret = (TraitDict) d1.MemberwiseClone();

      foreach(KeyValuePair<string, double> entry in d2)
      {
        if (ret.ContainsKey(entry.Key))
        {
          ret[entry.Key] += entry.Value;
        }
        else
        {
          ret[entry.Key] = entry.Value;
        }
      }
      return ret;
    }

  }

  public class Gene
  {
    public string name {get;}
    public string variant {get;}

    public Gene(string name, string variant)
    {
      this.name = name;
      this.variant = variant;
    }

    public override string ToString()
    {
      return name + ": " + variant;
    }
  }

  public abstract class GeneDist
  {
    public string name { get; }
    public string chromosome { get; }
    public double locus { get; }
    public double std { get; }
    public Dictionary<string, double> variants; // ("B", 0.1), ("b", 0.9)
    public double varSum;

    public GeneDist(string name,
                    string chromosome,
                    double locus,
                    double std,
                    Dictionary<string, double> variants)
    {
      this.name = name;
      this.chromosome = chromosome;
      this.locus = locus;
      this.std = std;
      this.variants = variants;
      this.varSum = 0;
      foreach(var val in variants.Values)
      {
        this.varSum += val;
      }
    }

    public abstract TraitDict EvalPairs(string[] pairs);
  }

  public class AccDist : GeneDist
  {
    public string trait;

    public AccDist(string name,
                    string chromosome,
                    double locus,
                    double std,
                    Dictionary<string, double> variants,
                    string trait)
                    : base(name, chromosome, locus, std, variants)
    {
      this.trait = trait;
    }

    public override TraitDict EvalPairs(string[] pairs)
    {
      TraitDict ret = new TraitDict();

      double sum = 0;
      foreach(string str in pairs)
      {
        if (str == "AA")
        {
          sum += 2;
        }
        else
        {
          sum++;
        }
      }

      ret[this.trait] = sum;
      return ret;
    }
  }

  public class Chromosome
  {
    public const int CromeLength = 100;

    public string name;
    public Gene[] left;
    public Gene[] right;

    public Chromosome(string name)
    {
      this.name = name;
      this.left = new Gene[CromeLength];
      this.right = new Gene[CromeLength];
    }
  }

  public class Genome : KeyedCollection<string, Chromosome>
  {
    protected override string GetKeyForItem(Chromosome chrome)
    {
        return chrome.name;
    }
  }


  public class Creature
  {
    public Genome genome;

    public Creature()
    {
      string[] test = {"morphology", "tissue", "psyche"};
      genome = new Genome();
      foreach (string chrome in test)
      {
        genome.Add(new Chromosome(chrome));
      }
    }

    public Creature(Species species)
    {
      genome = new Genome();

      // the order off adding here messes up distributions (overwrites), TODO fixing later
      foreach(var entry in species.geneList)
      {
        GeneDist dist = entry.dist;

        if(!genome.Contains(dist.chromosome))
        {
          genome.Add(new Chromosome(dist.chromosome));
        }

        double num = entry.weight * Chromosome.CromeLength * (RandGaussian(1.0, 0.1));

        if(num <= 0) continue;

        while(num > 1)
        {
          num -= 1;
          int loc = (int) Math.Round(RandGaussian(dist.locus, dist.std) * Chromosome.CromeLength);
          if (loc >= Chromosome.CromeLength) continue;
          bool left = UnityEngine.Random.value > 0.5 ? true : false;

          double select = UnityEngine.Random.value * dist.varSum;
          string variant = "";
          foreach(var vari in dist.variants)
          {
            if(select <= vari.Value)
            {
              variant = vari.Key;
              break;
            }
            select -= vari.Value;
          }
          if(left)
          {
            genome[dist.chromosome].left[loc] = new Gene(dist.name, variant);
          }
          else
          {
            genome[dist.chromosome].right[loc] = new Gene(dist.name, variant);
          }
        }
      }

    }
  }

  // temp main for test purposes
  class World
  {
    public static void Testrun()
    {
      GeneDist wool = new AccDist("wool",
                                  "tissue",
                                  0.6,
                                  0.1,
                                  new Dictionary<string, double>() {{"A", 1}},
                                  "fur");
      Species buffalos = new Species("buffalo");
      buffalos.AddGeneDist(wool, 0.55);

      Creature buff1 = new Creature(buffalos);
      Debug.Log("Hello!");
      Debug.Log(buff1.genome["tissue"].left[60]);

      //Creature test1 = new Creature();
      //Console.WriteLine("Hello");
      //Console.WriteLine(test1.genome["morphology"].left[0]);
    }
  }
}
