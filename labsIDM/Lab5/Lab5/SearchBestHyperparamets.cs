using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
using NeuralNetwork;
namespace Lab5
{
    internal class SearchBestHyperparamets
    {
        public static void main(int [] amountOfNodes, double[,] learningData, double[,] resultTestData, string FileName)
        {
            double min = 55;
            double min_stddev;
            double thebestlearningrate = 0;
            double mean = 0;
            double stddev = 0;
            NeuralNetwork.DataNeuralNetwork real_best = null;
            double real_mean = 100000;
            bool tryd = true;
            while (tryd)
            {
                for (double i = 0.05; i < 10; i *= 2.5)
                {
                    double[] results = new double[5];
                    for (int j = 0; j < 5; j++)
                    {
                        NeuralNetwork.NeuralNetwork neuralNetwork = new NeuralNetwork.NeuralNetwork(amountOfNodes);
                        TrainingData training = new TrainingData(linalg.Matrix<double>.Build.DenseOfArray(learningData), amountOfNodes[0], amountOfNodes[^1]);
                        NetworkTraining networkTraining = new NetworkTraining(ref neuralNetwork, training, NetworkTrainingStrategy.Backpropagation);
                        neuralNetwork.SetActivationStrategy(ActivationFunctionStrategy.Logistic);
                        networkTraining.SetLearningRate(i);
                        networkTraining.Train();
                        results[j] = Lab5.Lab5Things.Test(neuralNetwork, resultTestData).Item1;
                        System.Diagnostics.Debug.WriteLine(results[j]);
                        if (results[j] < real_mean)
                        {
                            real_best = neuralNetwork.GetDataAboutNetwork();
                            real_mean = results[j];
                        }
                    }
                    var res_vector = linalg.Vector<double>.Build.DenseOfArray(results);
                    mean = Lab5.Lab5Things.Mean(res_vector);
                    stddev = Lab5.Lab5Things.Stddev(res_vector);
                    if (mean < min)
                    {
                        min = mean;
                        thebestlearningrate = i;
                        min_stddev = stddev;
                    }
                    string result2 = mean.ToString();
                    System.Diagnostics.Debug.WriteLine("\n" + result2 + '\n');
                }
                Console.WriteLine($"Best result : { min.ToString()} for LearningRate : {thebestlearningrate}");
            }
            real_best.ToFile(FileName);
        }
    }
}
