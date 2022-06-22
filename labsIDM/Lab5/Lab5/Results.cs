using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
using NeuralNetwork;
namespace Lab5
{
    internal class Results
    {   
        public static void main(int[] amountOfNodes, double[,] learningData, double[,] verificationData, double[,] resultTestData, string FileName)
        {
            NeuralNetwork.NeuralNetwork neuralNetwork = new NeuralNetwork.NeuralNetwork(amountOfNodes);
            NeuralNetwork.DataNeuralNetwork real_best = neuralNetwork.GetDataAboutNetwork();
            real_best.FromFile(FileName);
            neuralNetwork.SetDataAboutNetwork(real_best);
            (double Loss, double F, double Mismatch) learningResult = Lab5.Lab5Things.Test(neuralNetwork, learningData),
                verificationResult = Lab5.Lab5Things.Test(neuralNetwork, verificationData),
                testResult = Lab5.Lab5Things.Test(neuralNetwork, resultTestData);
            Console.WriteLine($"Learning results:\nLoss function: {learningResult.Loss}\nF: {learningResult.F}\nMismatch: {learningResult.Mismatch}\n" +
                $"Verification results:\nLoss function: {verificationResult.Loss}\nF: {verificationResult.F}\nMismatch: {verificationResult.Mismatch}\n" +
                $"Test results:\nLoss function: {testResult.Loss}\nF: {testResult.F}\nMismatch: {testResult.Mismatch}");
        }
    }
}
