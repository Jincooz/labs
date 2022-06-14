#include <iostream>
#include "Repertoire.h"
using namespace std;

int main()
{
  Category category;
  int day, month, year, amountOfActors, troupeSalary, rentCost, amountOfSeats, orchestraSalary, rent, numPerfomances, categoryMarker, orchestra;
  string troupeName, apartamentName, apartamentAdress, perfomanceName;
  bool _orchestra;
  Apartment apartament;
  Trupe troupe;
  Date date;

  cout << "Input number of perfomances: ";
  cin >> numPerfomances;

  Performance* myPerfomances = new Performance[numPerfomances];
  for (int i = 0; i < numPerfomances; i++) 
  {
      cout << "Input name of perfomance: " << endl;
    cin >> perfomanceName;
    cout << "1 : Drama" << endl;
    cout << "2 : Operetta" << endl;
    cout << "3 : Opera" << endl;
    cout << "4 : Ballet" << endl;
    cout << "Input genre of perfomance: " << endl;
    while (true) {
        cin >> categoryMarker;
      switch (categoryMarker)
      {
      case 1:
      {
        category = Category::Drama;
        goto p;
      }
      case 2:
      {
        category = Category::Operetta;
        goto p;
      }
      case 3:
      {
        category = Category::Opera;
        goto p;
      }
      case 4:
      {
        category = Category::Ballet;
        goto p;
      }
      default:
        cout << "You wrote wrong genre, try again: " << endl;
        cin >> categoryMarker;
        break;
      }
    }
p:;
    cout << "Input name of apartament where perfomance is played: " << endl;
    cin >> apartamentName;
    cout << "Input adress of that apartament: " << endl;
    cin >> apartamentAdress;
    cout << "Input rent cost of apartament: " << endl;
    cin >> rentCost;
    cout << "Input amount of seats of apartament: " << endl;
    cin >> amountOfSeats;
    cout << "Input orchestra salary: " << endl;
    cin >> orchestraSalary;
    apartament = Apartment(apartamentName, apartamentAdress, rentCost, amountOfSeats);
    apartament.orchesterPrice = orchestraSalary;
    cout << "Input troupe's name: " << endl;
    cin >> troupeName;
    cout << "Input number of actors: " << endl;
    cin >> amountOfActors;
    cout << "Input salary of actors: " << endl;
    cin >> troupeSalary;
   troupe = Trupe(troupeName, amountOfActors, troupeSalary);
    cout << "Input perfomance day: " << endl;
    cin >> day;
    cout << "Input perfomance month: " << endl;
    cin >> month;
    cout << "Input perfomance year: " << endl;
    cin >> year;
    date = Date(day, month, year);
    cout << "Input rent of perfomance: " << endl;
    cin >> rent;
    cout << "Input if orchestra needed to play there (0, 1) " << endl;
    while (true) {
        cin >> orchestra;
        switch (orchestra)
        {
        case 0:
        {
            _orchestra = false;
            goto p2;
        }
        case 1:
        {
            _orchestra = true;
            goto p2;
        }
        default:
            cout << "Refill the answer";
            cin >> orchestra;
            break;
        } 
      }
p2:;
 

    Performance perfomance(perfomanceName, category, apartament, troupe, date, rent, _orchestra);
    myPerfomances[i] = perfomance;
  }
  Repertoire rep;
  Repertoire myRep = Repertoire("Grecee", myPerfomances);
  rep.ShowOnConsoleLong();
  myRep.ShowOnConsoleLong();
  Performance perf2;
  myRep.Add(perf2);
  myRep.ShowOnConsoleLong();
  myRep.ShowOnConsoleShort();

}
