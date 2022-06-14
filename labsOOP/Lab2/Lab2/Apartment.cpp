#include "Apartment.h"
#include <iostream>

int Apartment::orchesterPrice = 0;

int Apartment::GetOrendSum()
{
	return orendSum;
}

int Apartment::GetAmountOfSeats()
{
	return amountOfSeats;
}

std::string Apartment::GetTitle()
{
	return title;
}

std::string Apartment::GetAddress()
{
	return address;
}

Apartment& Apartment::SetTitle(std::string ntitle)
{
	title = ntitle;
	return *this;
}

Apartment& Apartment::SetAddress(std::string naddress)
{
	address = naddress;
	return *this;
}

Apartment& Apartment::SetOrendSum(int norendSum)
{
	orendSum = norendSum;
	return *this;
}

Apartment& Apartment::SetAmountOfSeats(int namountOfSeats)
{
	amountOfSeats = namountOfSeats;
	return *this;
}

Apartment::Apartment()
{
	SetTitle("a");
	SetAddress("bb b bb,4");
	SetOrendSum(1000);
	SetAmountOfSeats(20);
}

Apartment::Apartment(std::string ntitle, std::string naddress, int norendSum, int namountOfSeats)
{
	SetTitle(ntitle);
	SetAddress(naddress);
	SetOrendSum(norendSum);
	SetAmountOfSeats(namountOfSeats);
}

Apartment::Apartment(const Apartment& napartment)
{
	SetTitle(napartment.title);
	SetAddress(napartment.address);
	SetOrendSum(napartment.orendSum);
	SetAmountOfSeats(napartment.amountOfSeats);
}

Apartment::~Apartment(){}

void Apartment::ShowOnConsole()
{
	std::cout << "Title: " << title
		<< "\nAddress: " << address
		<< "\nOrdend sum: " << orendSum
		<< "\nAmount of seats: " << amountOfSeats << std::endl;
}
