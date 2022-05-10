using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
using NeuralNetwork;
namespace Lab5
{
    internal class Lab5Things
    {
        internal static (double, double) Test(NeuralNetwork.NeuralNetwork neuralNetwork, double[,] testData)
        {
            double TP = 0, FP = 0, FN = 0, TN =0, F = 0;
            double result = 0;
            TrainingData trainingData = new TrainingData(linalg.Matrix<double>.Build.DenseOfArray(testData), 7, 1);
            foreach (var data in trainingData.Data)
            {
                var diference = (normalize(neuralNetwork.ActivateNeuralNetwork(data[0].ToArray())) - data[1]);
                if (diference[0] != 0)
                {
                    if(data[1][0] != 0)
                    {
                        FP++;
                    }else
                    {
                        FN++;
                    }
                }else
                {
                    if (data[1][0] != 0)
                    {
                        TP++;
                    }
                    else
                    {
                        TN++;
                    }
                }
                result += Pow(diference).Sum() / data[1].Count;
            }
            double P = (TP / (TP + FP)), R = (TP / (TP + FN));
            F = 2d * P * R /(P + R);
            return (result / trainingData.Data.Count, F);

        }

        internal static double Mean(linalg.Vector<double> x)
        {
            return x.Average();
        }
        internal static double Stddev(linalg.Vector<double> x)
        {
            double result = 0;
            double mean = Mean(x);
            for (int i = 0; i < x.Count; i++)
            {
                result += (x[i] - mean) * (x[i] - mean);
            }
            return result / x.Count;
        }

        internal static double[,] GetDataFromFile(string path, int amountOfDataInRow)
        {
            string[] trainingData = File.ReadAllLines(path);
            double[,] data = new double[trainingData.Length, amountOfDataInRow];
            for (int i = 0; i < trainingData.Length; i++)
            {
                string[] trainDataRow = trainingData[i].Split('\\');
                for (int j = 0; j < trainDataRow.Length; j++)
                {
                    data[i, j] = double.Parse(trainDataRow[j]);
                }
            }
            return data;
        }

        internal static linalg.Vector<double> Pow(linalg.Vector<double> value)
        {
            linalg.Vector<double> result = value.Clone();
            for (int i = 0; i < value.Count; i++)
            {
                result[i] = value[i] * value[i];
            }
            return result;
        }

        internal static linalg.Vector<double> normalize(linalg.Vector<double> value)
        {
            for (int i = 0; i < value.Count; i++)
            {
                value[i] = value[i] > 0.5 ? 1 : value[i] < 0.5 ? 0 : value[i];
            }
            return value;
        }
    }
}
