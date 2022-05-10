using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
using NeuralNetwork;
namespace Lab5
{
    internal class Results
    {
        public static void main(int[] amountOfNodes, double[,] learningData, double[,] resultTestData, string FileName)
        {
            NeuralNetwork.NeuralNetwork neuralNetwork = new NeuralNetwork.NeuralNetwork(amountOfNodes);
            NeuralNetwork.DataNeuralNetwork real_best = neuralNetwork.GetDataAboutNetwork();
            real_best.FromFile(FileName);
            neuralNetwork.SetDataAboutNetwork(real_best);
            (double, double) learningResult = Lab5.Lab5Things.Test(neuralNetwork, learningData),
                testResult = Lab5.Lab5Things.Test(neuralNetwork, resultTestData);
            Console.WriteLine($"Learning results:\nDispersion: {learningResult.Item1}\nF: {learningResult.Item2}\n" +
                $"Test results:\nDispersion: {testResult.Item1}\nF: {testResult.Item2}");
        }
    }
}
