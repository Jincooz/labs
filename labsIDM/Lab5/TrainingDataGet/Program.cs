// See https://aka.ms/new-console-template for more information
Random random = new Random(DateTime.Now.Second);
double credit_base;//10000-1000000
double salary;//15000-3000000
double persent;// 0.1-2
bool conections;// True False
double howmany_haveCredits;// 0 0.5 1 1.5 2
bool country_factor;// True False
double country_stability;//0 0.25 0.5 0.75 1
using StreamWriter file = new("Training.txt", append: true);
bool cycle = true;
while (cycle)
{
    Console.Clear();
    credit_base = random.NextDouble()*990000+10000;//10000-1000000
    salary = random.NextDouble()*2900000+100000;//100000-3000000
    persent = random.NextDouble() * 2.9 + 0.1;// 0.1-2
    conections = random.NextDouble()>0.5;// True False
    howmany_haveCredits = (random.NextDouble()>0.9)?0d:((random.NextDouble() > 0.7) ? 0.5 : ((random.NextDouble() > 0.5) ? 1d : ((random.NextDouble() > 0.3) ? 1.5 : 2d)));// 0 0.5 1 1.5 2
    country_factor = (random.NextDouble() > 0.9);// True False
    country_stability = random.NextDouble();//0 0.25 0.5 0.75 1
    Console.WriteLine($"Credit for {credit_base}\nHis salary {salary}\n" +
        $"Percent  {persent}\nHe "+(conections?"has":"dont have")+" conection\n" +
        $"He have {howmany_haveCredits*2} credits\nHe have "+(country_factor?"right":"wrong")+" country\n" +
        $"Our couuntry stability {country_stability}");
    ConsoleKeyInfo key = Console.ReadKey();
    double[] result = new double[3];
    switch (key.Key)
    {
        case ConsoleKey.Escape:
            cycle = false;
            break;
        case ConsoleKey.D1:
            result[0] = 1d;
            result[1] = 0;
            result[2] = 0;
            break;
        case ConsoleKey.D2:
            result[0] = 0.5;
            result[1] = 0.5;
            result[2] = 0;
            break;
        case ConsoleKey.D3:
            result[0] = 0;
            result[1] = 1;
            result[2] = 0;
            break;
        case ConsoleKey.D4:
            result[0] = 0;
            result[1] = 0.5;
            result[2] = 0.5;
            break;
        case ConsoleKey.D5:
            result[0] = 0;
            result[1] = 0;
            result[2] = 1;
            break;
        default:
            continue;
            break;
    }
    double result_credit = credit_base * (1 + persent) / salary / 3;
    double result_Creditscount = howmany_haveCredits / 2.0d;
    string resultstr = result_credit.ToString() + "\\" + (persent / 2.0).ToString() + "\\" + (conections ? 1 : 0).ToString() + "\\" + result_Creditscount.ToString() + "\\" + (country_factor ? 1 : 0).ToString() + "\\" + country_stability.ToString() + "|" + result[0].ToString() + "\\" + result[1].ToString() + "\\" + result[2].ToString();
    await file.WriteLineAsync(resultstr);
}