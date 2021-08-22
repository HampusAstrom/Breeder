using System;
using UnityEngine;

public class Util
{
  public static double RandGaussian(double mean = 0.0, double std = 1.0)
  {
    double u, v, s;

    do
    {
        u = 2.0 * UnityEngine.Random.value - 1.0;
        v = 2.0 * UnityEngine.Random.value - 1.0;
        s = u * u + v * v;
    }
    while (s >= 1.0);

    // Standard Normal Distribution
    s = u * Math.Sqrt(-2.0 * Math.Log(s) / s);

    return mean + s * std;
  }
}
