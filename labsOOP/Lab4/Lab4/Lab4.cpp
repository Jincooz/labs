#include <iostream>
#include "Repertoire.h"
using namespace std;

int main()
{
	Date firstDate, secondDate;
	int day, month, year;
	cout << "First date:" << endl;
	cout << "Day: ";
	cin >> day;
	cout << "Month: ";
	cin >> month;
	cout << "Year: ";
	cin >> year;
	firstDate = Date(day, month, year);
	cout << "Second date: (\"Day Month Year\") " << endl;
	cin >> secondDate;
	cout << firstDate;
	cout << secondDate;
	cout << firstDate + secondDate;
	Apartment firstApartment, secondApartment;
	int orendSum, amountOfSeats;
	string title, address;
	cout << "First apartment:" << endl;
	cout << "OrendSum: ";
	cin >> orendSum;
	cout << "AmountOfSeats: ";
	cin >> amountOfSeats;
	cout << "Title: ";
	cin >> title;
	cout << "Address: ";
	cin >> address;
	firstApartment = Apartment(title, address, orendSum, amountOfSeats);
	cout << "Second apartment: (\"title address orendSum amountOfSeats\")" << endl;
	cin >> secondApartment;
	cout << firstApartment;
	cout << secondApartment;
	cout << (firstApartment == secondApartment ? "Equal" : "Not equal");
	cout << (firstApartment > secondApartment ? "First bigger" : (firstApartment != secondApartment ? "Second bigger" : "Equal"));
}
