using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using MathNet.Numerics;
namespace CM_9
{
    class Finite_Diff
    {
        //граничные условия
        public static double
            a = 1.3d, b = 1.6d,
            A = 0.6d, B = 0.3d;
        public static (double, double) alpha = (1.5d, -1d), beta = (2, 0);
        public static double p(double x) { return -0.25d; }
        public static double q(double x) { return 2d / x; }
        public static double f(double x) { return x / 2; }
        public static int getn(double h)
        {
            return (int)((b - a) / h);
        }
        public static void finite_diff(double h)
        {
            var n = getn(h);
            Console.WriteLine(@"Step is {0}", h);
            var x = MathNet.Numerics.LinearAlgebra.Vector<double>.Build.Dense(n + 1, 0);
            for (int i = 0; i < n + 1; i++)
            {
                x[i] = a + i * h;
            }
            var C = MathNet.Numerics.LinearAlgebra.Matrix<double>.Build.Dense(n + 1, n + 1, 0);
            var d = MathNet.Numerics.LinearAlgebra.Vector<double>.Build.Dense(n + 1, 0);
            C[0, 0] = alpha.Item1 * h - alpha.Item2;
            C[0, 1] = alpha.Item2;
            C[n, n - 1] = -beta.Item2;
            C[n, n] = beta.Item1 * h + beta.Item2;
            for (int i = 1; i < n; i++)
            {
                C[i, (i - 1)] = 1 - h * p(x[i]) / 2;
                C[i, i] = h * h * q(x[i]) - 2;
                C[i, (i + 1)] = 1 + h * p(x[i]) / 2;
            }
            d[0] = A * h;
            d[n] = B * h;
            for (int i = 1; i < n; i++)
            {
                d[i] = f(x[i]) * h * h;
            }
            var y = C.Solve(d);
            for(int i = 0;i<n+1;i++)
            {
                Console.WriteLine(Math.Round(x[i],3).ToString() + "\t" + Math.Round(y[i],3).ToString() + "\t" + Math.Round(Analytic(x[i]), 3).ToString());
            }
            return;
        }
        static double Analytic(double x)
        {
            double s1 = (2.87494 * Math.Pow(10, -10) * Math.Pow(x,7) 
                - 6.43987* Math.Pow(10, -8) * Math.Pow(x, 6) 
                + 5.40949* Math.Pow(10, -6) * Math.Pow(x, 5) 
                - 0.00021638 * Math.Pow(x, 4) 
                + 0.00432759 * Math.Pow(x, 3)
                - 0.0415449 * Math.Pow(x, 2) 
                + 0.166179 * x - 0.189919);
            double s2 = (-2.26499 * Math.Pow(10, -9) * Math.Pow(x, 7) 
                + 5.07358 * Math.Pow(10, -7) * Math.Pow(x, 6) 
                - 0.0000426181 * Math.Pow(x, 5)
                + 0.00170472 * Math.Pow(x, 4)
                - 0.0340945 * Math.Pow(x, 3)
                + 0.327307 * Math.Pow(x, 2)
                - 0.975894 * x + 1.11531);
            double s3 = (-1.14998 * Math.Pow(10, -9) * Math.Pow(x, 7)
                + 2.52995 * Math.Pow(10, -7) * Math.Pow(x, 6)
                - 0.0000206444 * Math.Pow(x, 5)
                + 0.000786768 * Math.Pow(x, 4)
                - 0.0144489 * Math.Pow(x, 3)
                + 0.117767 * Math.Pow(x, 2)
                - 0.326254 * x + 0.0949597);
            double expint = SpecialFunctions.ExponentialIntegral(x / 4, 7);
            double r1 = x * s1 * expint;
            double r2 = x * s2;
            double r3 = Math.Exp(x / 4) * s3;
            return r1
                + r2
                + r3; 
        }


        static void Main(string[] args)
        {
            finite_diff(0.05d);
            Console.ReadKey(true);
        }
    }
}

