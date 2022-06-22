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
	std::cout << "!!!! Constructor Apartment no parametrs" << std::endl;
	SetTitle("a");
	SetAddress("bb b bb,4");
	SetOrendSum(1000);
	SetAmountOfSeats(20);
}

Apartment::Apartment(std::string ntitle, std::string naddress, int norendSum, int namountOfSeats)
{
	std::cout << "!!!! Constructor Apartment with parametrs" << std::endl;
	SetTitle(ntitle);
	SetAddress(naddress);
	SetOrendSum(norendSum);
	SetAmountOfSeats(namountOfSeats);
}

Apartment::Apartment(const Apartment& napartment)
{
	std::cout << "!!!! Copy constructor Apartment" << std::endl;
	SetTitle(napartment.title);
	SetAddress(napartment.address);
	SetOrendSum(napartment.orendSum);
	SetAmountOfSeats(napartment.amountOfSeats);
}

Apartment::~Apartment(){
	std::cout << "!!!! Destructor Apartment" << std::endl;
}

void Apartment::ShowOnConsole()
{
	std::cout << "Title: " << title
		<< "\nAddress: " << address
		<< "\nOrdend sum: " << orendSum
		<< "\nAmount of seats: " << amountOfSeats << std::endl;
}

bool Apartment::operator>(const Apartment value)
{
	return this->amountOfSeats > value.amountOfSeats;
}

bool Apartment::operator<(const Apartment value)
{
	return this->amountOfSeats < value.amountOfSeats;
}

bool Apartment::operator==(const Apartment value)
{
	bool result = (value.address == this->address) && 
		(value.title == this->title) && 
		(value.amountOfSeats == this->amountOfSeats) && 
		(value.orendSum == this->orendSum);
	return result;
}

bool Apartment::operator!=(const Apartment value)
{
	bool result = (value.address == this->address) &&
		(value.title == this->title) &&
		(value.amountOfSeats == this->amountOfSeats) &&
		(value.orendSum == this->orendSum);
	return !result;
}

std::ostream& operator<< (std::ostream& out, const Apartment& value)
{
	out << "Title: " << value.title
		<< "\nAddress: " << value.address
		<< "\nOrdend sum: " << value.orendSum
		<< "\nAmount of seats: " << value.amountOfSeats << std::endl;
	return out;
}

std::istream& operator>>(std::istream& in, Apartment& value)
{
	in >> value.title >> value.address >> value.orendSum >> value.amountOfSeats;
	return in;
}