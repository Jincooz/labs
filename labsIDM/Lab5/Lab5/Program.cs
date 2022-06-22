int[] amountOfNodes = { 7, 5, 1 };
double[,] learningData = Lab5.Lab5Things.GetDataFromFile("Training1.txt", amountOfNodes[0] + amountOfNodes[^1]);
double[,] verificationData = Lab5.Lab5Things.GetDataFromFile("Training2.txt", amountOfNodes[0] + amountOfNodes[^1]);
double[,] resultTestData = Lab5.Lab5Things.GetDataFromFile("Training3.txt", amountOfNodes[0]+amountOfNodes[^1]);
string FileName = "Result1.txt"; 
//Lab5.SearchBestHyperparamets.main(amountOfNodes, learningData, resultTestData, FileName);
Lab5.Results.main(amountOfNodes, learningData, verificationData, resultTestData, FileName);
