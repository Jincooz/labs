// See https://aka.ms/new-console-template for more information
using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
Console.WriteLine("Hello, World!");
int[] amountOfNodes = { 3, 2 };
Lab5.NeuralNetwork neuralNetwork = new Lab5.NeuralNetwork(amountOfNodes);
double[] vs = { 1d, 2d, 3d };
Console.WriteLine(neuralNetwork.ActivateNeuralNetwork(vs));
Console.ReadKey();

namespace Lab5
{
    class NeuralNetwork
    {
        private readonly List<int>? _amountOfNodes;
        private List<linalg.Matrix<double>> _weightMatrices = new List<linalg.Matrix<double>>();
        private List<linalg.Vector<double>> _biases = new List<linalg.Vector<double>>();
        private List<linalg.Vector<double>> _layers = new List<linalg.Vector<double>>();
        private linalg.Vector<double>? _inputLayer;
        private linalg.Vector<double>? _outputLayer;
        public linalg.Vector<double>? InputLayer { get { return _inputLayer; } set { _inputLayer = value; } }
        public linalg.Vector<double>? OutputLayer { get { return _outputLayer; } }
        private linalg.Matrix<double> XavierWeightInitialization(int numberOfNeronsInPreviusLayer, int numberOfNeronsInThisLayer, Random rand)
        {
            //uniform probability distribution in (-1/sqrt(n),1/sqrt(n)), where n - amount of neuron in previuse layer
            double lower = -(1.0 / Math.Sqrt(numberOfNeronsInPreviusLayer)), upper = (1.0 / Math.Sqrt(numberOfNeronsInPreviusLayer));
            return linalg.Matrix<double>.Build.Dense(numberOfNeronsInThisLayer, numberOfNeronsInPreviusLayer, lower + rand.NextDouble() * (upper - lower));
        }
        public NeuralNetwork(List<int> amountOfNodes)
        {
            Clear();
            _amountOfNodes = amountOfNodes;
            _inputLayer = linalg.Vector<double>.Build.Dense(amountOfNodes[0], 0.0);
            _outputLayer = linalg.Vector<double>.Build.Dense(amountOfNodes[amountOfNodes.Count - 1], 0.0);
            Random rand = new Random(DateTime.Now.Second);
            for (int i = 0; i < amountOfNodes.Count; i++)
            {
                _layers.Add(linalg.Vector<double>.Build.Dense(amountOfNodes[i], 0.0));
                if (i != 0)
                {
                    _weightMatrices.Add(XavierWeightInitialization(numberOfNeronsInPreviusLayer: amountOfNodes[i - 1], numberOfNeronsInThisLayer: amountOfNodes[i], rand: rand));
                    _biases.Add(linalg.Vector<double>.Build.Dense(amountOfNodes[i], 0));
                }
            }
        }
        public NeuralNetwork(int[] amountOfNodes) : this(new List<int>(amountOfNodes)) { }
        private NeuralNetwork(List<int> amountOfNodes, List<linalg.Matrix<double>> weightMatrices) : this(amountOfNodes)
        {
            _weightMatrices = weightMatrices;
        }
        public void Clear()
        {
            _weightMatrices = new List<linalg.Matrix<double>>();
            _layers = new List<linalg.Vector<double>>();
            _biases = new List<linalg.Vector<double>>();
            _inputLayer = null;
            _outputLayer = null;
        }
        public linalg.Vector<double> ActivationFunction(linalg.Vector<double> value)
        {
            //sigmoid
            for (int i = 0; i < value.Count; i++)
            { 
                value[i] = 1/(1+Math.Exp(-value[i]));
            }
            return value;
        }
        public linalg.Vector<double>? ActivateNeuralNetwork(linalg.Vector<double> inputLayer)
        {
            _inputLayer = inputLayer;
            return ActivateNeuralNetwork();
        }
        public linalg.Vector<double>? ActivateNeuralNetwork(double[] inputLayer)
        {
            _inputLayer = linalg.Vector<double>.Build.DenseOfArray(inputLayer);
            return ActivateNeuralNetwork();
        }
        public linalg.Vector<double>? ActivateNeuralNetwork()
        {
            if (_inputLayer == null)
                return null;
            _layers[0] = _inputLayer;
            for (int i = 0; i < _layers.Count - 1; i++)
            {
                linalg.Vector<double> value = _weightMatrices[i] * _layers[i] + _biases[i];
                _layers[i + 1] = ActivationFunction(_weightMatrices[i] * _layers[i] + _biases[i]);
            }
            _outputLayer = _layers[_layers.Count - 1];
            return _outputLayer;
        }
    }
}