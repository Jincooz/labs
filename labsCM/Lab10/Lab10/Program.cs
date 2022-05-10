using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MathNet.Numerics;
using MathNet.Numerics.LinearAlgebra;

namespace CH_M_10
{
    class ElipticEqyation
    {
        public static double StartX = 0.0d;
        public static double h = 1.0d;
        public static double GammaAr(double x, double y)
        {
            return 0.5 * (Math.Abs(x) + Math.Abs(y));
        }
        public static double GetFunc(double x)
        {
            return 3 * Math.Sqrt(1 - Math.Pow(x, 2) / 16);
        }
        public static double GetFuncInv(double y)
        {
            return 4 * Math.Sqrt(1 - Math.Pow(y, 2) / 9);
        }
        public static int getsize(double start, double h)
        {
            var test = new double();
            var n = 0;
            do
            {
                test = 1 - Math.Pow(start, 2) / 16;
                start += h;
                n++;
            } while (test >= 0);
            return n - 1;
        }
        public static Matrix<double> CoefField = Matrix<double>.Build.Dense(getsize(StartX, h) - 1, getsize(StartX, h));
        public static Vector<double> Y = Vector<double>.Build.Dense(getsize(StartX, h));
        public static Vector<double> X = Vector<double>.Build.Dense(getsize(StartX, h));
        public static void ConstructField()
        {
            var x = new double();
            var y = new int();
            var sum = 0.0d;
            var j = 0;
            var indicator = 0;
            var size = getsize(StartX, h) - 1;
            // Console.WriteLine(size);
            x = StartX;
            for (int i = 0; i < size + 1; i++)
            {
                Y[i] = GetFunc(x);
                X[i] = x;
                //Console.WriteLine(X[i]);
                x += h;
            }
            do
            {
                y = (int)Math.Round(Y[j], 0);
                //Console.WriteLine(y);
                CoefField[size - y - 1, j] = Math.Round(GammaAr(X[j], Y[j]), 2);
                j++;
            } while (j < size + 1);
            j = 0;
            for (int k = 0; k < size; k++)
            {
                sum = 0;
                for (int p = 0; p < size + 1; p++)
                {
                    sum += CoefField[k, p];
                }
                if (sum != 0)
                {
                    indicator = k;
                    x = GetFuncInv(k);
                    CoefField[size - k - 1, (int)Math.Round(x, 0)] = Math.Round(GammaAr(k, x), 2);
                }
            }
            for (int i = 0; i < size; i++)
            {
                for (int p = 0; p < size + 1; p++)
                {
                    if (CoefField[i, p] == 0)
                    {
                        //CoefField[i, p] = (double)(j+1) / 100;
                        j++;
                    }
                    else break;
                }
            }
            Console.WriteLine("Basic Template (only bounded values)");
            for (int i = 0; i < size; i++)
            {
                for (int k = 0; k < size + 1; k++)
                {
                    Console.Write(Math.Round(CoefField[i, k], 2) + " ");
                }
                Console.WriteLine();
            }
            Matrix<double> SystemtoSolve = Matrix<double>.Build.DenseOfArray(new double[,]
            {
                {4,-2,0,-1,0,0,0,0,0,0,0 },
                {-1,4,-1,0,-1,0,0,0,0,0,0 },
                {0,-1,4,0,0,-1,0,0,0,0,0 },
                {-1,0,0,4,-2,0,0,-1,0,0,0 },
                {0,-1,0,-1,4,-1,0,0,-1,0,0 },
                {0,0,-1,0,-1,4,-1,0,0,-1,0 },
                {0,0,0,0,0,-1,4,0,0,0,1 },
                {0,0,0,0,-4,0,0,4,0,0,0 },
                {0,0,0,0,-2,0,0,-1,4,-1,0 },
                {0,0,0,0,0,-2,0,0,-1,4,-1 },
                {0,0,0,0,0,-2,0,0,0,0,4 }
            }
                );
            Vector<double> Vectorr = Vector<double>.Build.DenseOfArray(new double[] { 1.5, 1.95, 4.79, 0, 0, 0, 4.88, 0, 0, 0, 4.78 });
            var solution = SystemtoSolve.Solve(Vectorr);
            /*for (int i = 0; i < j; i++)
            {
                for (int k = 0; k <j; k++)
                {
                    Console.Write(SystemtoSolve[i, k] + " ");
                }
                Console.WriteLine();
            }
            for (int k = 0; k < j; k++)
            {
                Console.Write(Vectorr[k]+" ");
            }
            Console.WriteLine();
            for (int k = 0; k < j; k++)
            {
                Console.Write(Math.Round(solution[k],2) + " ");
            }
            Console.WriteLine();
           */
            var itr = 0;
            for (int i = 0; i < size; i++)
            {
                for (int p = 0; p < size + 1; p++)
                {
                    if (CoefField[i, p] == 0)
                    {
                        CoefField[i, p] = Math.Round(solution[itr], 2);
                        itr++;
                    }
                    else break;
                }
            }
            Console.WriteLine("Template WITHOUT iterations (inner values included)");
            for (int i = 0; i < size; i++)
            {
                for (int k = 0; k < size + 1; k++)
                {
                    Console.Write(CoefField[i, k] + " ");
                }
                Console.WriteLine();
            }

        }

        static void Main(string[] args)
        {
            ConstructField();
            Console.WriteLine("POSTAVTE ZACHET POJALUISTA");
        }
    }
}
