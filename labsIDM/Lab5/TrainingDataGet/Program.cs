// See https://aka.ms/new-console-template for more information
Random random = new Random(DateTime.Now.Second);
double credit_base;//10000-1000000
double salary;//15000-3000000
double persent;// 0.1-2
bool conections;// True False
double howmany_haveCredits;// 0 0.5 1 1.5 2
bool country_factor;// True False
double country_stability;//0 0.25 0.5 0.75 1
double pledge;
using StreamWriter file = new("Training.txt", append: true);
bool cycle = true;
while (cycle)
{
    Console.Clear();
    credit_base = random.NextDouble()*990000+10000;//10000-1000000
    salary = random.NextDouble()*2900000+100000;//100000-3000000
    persent = random.NextDouble() * 2.9 + 0.1;// 0.1-3
    conections = random.NextDouble()>0.5;// True False
    howmany_haveCredits = (random.NextDouble()>0.9)?0d:((random.NextDouble() > 0.7) ? 0.5 : ((random.NextDouble() > 0.5) ? 1d : ((random.NextDouble() > 0.3) ? 1.5 : 2d)));// 0 0.5 1 1.5 2
    country_factor = (random.NextDouble() > 0.9);// True False
    pledge = random.NextDouble() > 0.5 ? 1 : 0;
    country_stability = random.NextDouble();//0 0.25 0.5 0.75 1
    Console.WriteLine($"Credit for {credit_base}\nHis official salary {salary}\n" +
        $"Percent {persent}\nOur income from this {credit_base*persent}\n" +
        $"Diferense: {-credit_base * (1 + persent) + salary}\nHe "+(conections?"has":"dont have")+" conection\n" +
        $"He have {howmany_haveCredits*2} credits\nHe have "+(country_factor?"right":"wrong")+" country\n" +
        $"His pledge {pledge}\nOur couuntry stability {country_stability}");
    ConsoleKeyInfo key = Console.ReadKey();
    double[] result = new double[1];
    switch (key.Key)
    {
        case ConsoleKey.Escape:
            cycle = false;
            break;
        case ConsoleKey.D1:
            result[0] = 1d;
            break;
        case ConsoleKey.D2:
            result[0] = 0;
            break;
        default:
            continue;
            break;
    }
    double result_credit = credit_base * (1 + persent) / salary;
    double result_Creditscount = howmany_haveCredits / 2.0d;
    string resultstr = 
        result_credit.ToString() + "\\" 
        + (persent / 2.0).ToString() 
        + "\\" + (conections ? 1 : 0).ToString() 
        + "\\" + result_Creditscount.ToString() 
        + "\\" + (country_factor ? 1 : 0).ToString() 
        + "\\" + country_stability.ToString() 
        + "\\" + pledge.ToString()
        + "\\" + result[0].ToString();
    await file.WriteLineAsync(resultstr);
}