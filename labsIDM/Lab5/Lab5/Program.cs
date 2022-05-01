// See https://aka.ms/new-console-template for more information
using num = MathNet.Numerics;
using linalg = MathNet.Numerics.LinearAlgebra;
int[] amountOfNodes = { 3, 2 };
Lab5.NeuralNetwork neuralNetwork = new Lab5.NeuralNetwork(amountOfNodes);
double[] vs = { 1d, 2d, 3d };
Console.WriteLine(neuralNetwork.ActivateNeuralNetwork(vs));
Console.ReadKey();

namespace Lab5
{
    class NeuralNetwork
    {
        private class TrainingData
        {
            private readonly int _inputNodesAmount, _outputNodesAmount;
            private readonly int _amountOfRecordsInDataset;
            private readonly List<linalg.Vector<double>[]> _data;
            private int _amountOfData;
            private List<List<linalg.Vector<double>[]>> _datasets;
            private int _amountOFDatasets;
            public int AmountOfRecordsInDataset { get { return _amountOfRecordsInDataset; } }
            public List<List<linalg.Vector<double>[]>> DataSets { get { return _datasets; } }
            public int CountDatasets { get { return _amountOFDatasets; } }
            public TrainingData(linalg.Matrix<double> trainingData, int groupBy, int inputNodesAmount, int outputNodesAmount)
            {
                _amountOfRecordsInDataset = groupBy;
                _inputNodesAmount = inputNodesAmount;
                _outputNodesAmount = outputNodesAmount;
                _amountOfData = 0;
                _amountOFDatasets = 0;
                _data = new List<linalg.Vector<double>[]>();
                AddData(trainingData);
            }
            public void AddData(linalg.Matrix<double> newTrainingData)
            {
                for (int i = 0; i < newTrainingData.RowCount; i++)
                {
                    linalg.Vector<double>[] newRecord = new linalg.Vector<double>[2];
                    newRecord[0] = linalg.Vector<double>.Build.Dense(_inputNodesAmount, 0);
                    newRecord[1] = linalg.Vector<double>.Build.Dense(_outputNodesAmount, 0);
                    for (int j = 0; j < _inputNodesAmount + _outputNodesAmount; j++)
                    {
                        if (i < _inputNodesAmount)
                            newRecord[0][j] = newTrainingData[i, j];
                        else
                            newRecord[1][j] = newTrainingData[i, j];
                    }
                    _data.Add(newRecord);
                    _amountOfData++;
                }
                DivideDataInDatasets();
            }
            private void DivideDataInDatasets()
            {
                _datasets = new List<List<linalg.Vector<double>[]>>();
                for (int i = 0; i < _amountOfData / _amountOfRecordsInDataset; i++)
                {
                    List<linalg.Vector<double>[]> newDataset = new List<linalg.Vector<double>[]>();
                    for (int j = 0; j < _amountOfRecordsInDataset; j++)
                    {
                        newDataset.Add(_data[i * _amountOfRecordsInDataset + j]);
                    }
                    _datasets.Add(newDataset);
                    _amountOFDatasets++;
                }
            }
        }
        private TrainingData _trainingData;
        private readonly List<int>? _amountOfNodes;
        private List<linalg.Matrix<double>> _weightMatrices = new List<linalg.Matrix<double>>();
        private List<linalg.Vector<double>> _biases = new List<linalg.Vector<double>>();
        private List<linalg.Vector<double>> _layers = new List<linalg.Vector<double>>();
        private linalg.Vector<double>? _inputLayer;
        private linalg.Vector<double>? _outputLayer;
        public linalg.Vector<double>? InputLayer { get { return _inputLayer; } set { _inputLayer = value; } }
        public linalg.Vector<double>? OutputLayer { get { return _outputLayer; } }
        private linalg.Matrix<double> XavierWeightInitialization(int numberOfNeronsInPreviusLayer, int numberOfNeronsInThisLayer)
        {
            //uniform probability distribution in (-1/sqrt(n),1/sqrt(n)), where n - amount of neuron in previuse layer
            Random rand = new Random(DateTime.Now.Second);
            double lower = -(1.0 / Math.Sqrt(numberOfNeronsInPreviusLayer)), upper = (1.0 / Math.Sqrt(numberOfNeronsInPreviusLayer));
            var matrix = linalg.Matrix<double>.Build.Dense(numberOfNeronsInThisLayer, numberOfNeronsInPreviusLayer, 0);
            for (int i = 0; i < matrix.RowCount; i++)
            {
                for (int j = 0; j < matrix.ColumnCount; j++)
                {
                    matrix[i, j] = lower + rand.NextDouble() * (upper - lower);
                }
            }
            return matrix;
        }
        public NeuralNetwork(List<int> amountOfNodes)
        {
            Clear();
            _amountOfNodes = amountOfNodes;
            _inputLayer = linalg.Vector<double>.Build.Dense(amountOfNodes[0], 0.0);
            _outputLayer = linalg.Vector<double>.Build.Dense(amountOfNodes[amountOfNodes.Count - 1], 0.0);
            for (int i = 0; i < amountOfNodes.Count; i++)
            {
                _layers.Add(linalg.Vector<double>.Build.Dense(amountOfNodes[i], 0.0));
                if (i != 0)
                {
                    _weightMatrices.Add(XavierWeightInitialization(numberOfNeronsInPreviusLayer: amountOfNodes[i - 1], numberOfNeronsInThisLayer: amountOfNodes[i]));
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
                value[i] = 1 / (1 + Math.Exp(-value[i]));
            }
            return value;
        }
        private linalg.Vector<double> ActivationFunctionDerivative(linalg.Vector<double> value)
        {
            //sigmoid*(1-sigmoid)
            for (int i = 0; i < value.Count; i++)
            {
                value[i] = (1 / (1 + Math.Exp(-value[i]))) * (1 - 1 / (1 + Math.Exp(-value[i])));
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
        private void SetTrainingData(linalg.Matrix<double> trainingData, int groupBy = 10)
        {
            _trainingData = new TrainingData(trainingData, groupBy, inputNodesAmount: _amountOfNodes[0], outputNodesAmount: _amountOfNodes[^-1]);
        }
        public void AddTrainingData(linalg.Matrix<double> trainingData, int groupBy = 10)
        {
            if (trainingData.ColumnCount != _amountOfNodes[0] + _amountOfNodes[^1])
            {//list size = (n+m)*amount of data
                //TODO Try do this error better
                throw new InvalidOperationException("Training data don`t math NeuralNetwork");
            }
            if (_trainingData == null)
            {
                SetTrainingData(trainingData, groupBy);
                return;
            }
            _trainingData.AddData(trainingData);
        }
        public void TrainNeuralNetwork()
        {
            for (int i = 0; i < _trainingData.CountDatasets; i++)
            {
                //count mean of Gradients
                List<linalg.Matrix<double>> gradientWeights = new List<linalg.Matrix<double>>();
                //same shape as _weightMatrices
                List<linalg.Vector<double>> gradientBiases = new List<linalg.Vector<double>>();
                //same shape as _biases
                for (int j = 1; i < _amountOfNodes.Count; i++)
                {
                    gradientWeights.Add(linalg.Matrix<double>.Build.Dense(_amountOfNodes[i - 1], _amountOfNodes[i], 0));
                    gradientBiases.Add(linalg.Vector<double>.Build.Dense(_amountOfNodes[i], 0));
                }
                List<linalg.Vector<double>[]> dataset = _trainingData.DataSets[i];
                for (int j = 0; j < _trainingData.AmountOfRecordsInDataset; j++)
                {
                    var input = dataset[j][0];
                    var desireOutput = dataset[j][1];
                    var networkOutput = ActivateNeuralNetwork(input);
                    var diference = networkOutput - desireOutput;
                    for (int k = gradientWeights.Count - 1; k >= 0; k--)
                    {
                        //double dCdz = 2 * diference * ActivationFunctionDerivative((_weightMatrices[k] * _layers[k] + _biases[k])[]);
                        for (int l = 0; l < gradientWeights[k].RowCount; l++)
                        {
                            for (int m = 0; m < gradientWeights[k].ColumnCount; m++)
                            {

                            }
                        }
                    }

                }
                //TODO add -gradient
            }
        }
    }
}