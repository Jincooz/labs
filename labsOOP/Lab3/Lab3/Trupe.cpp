#include "Trupe.h"
#include <iostream>
int Trupe::GetActorsAmount()
{
	return amountOfActors;
}

int Trupe::GetPayMoneyAmount()
{
	return sumMoneyForActors;
}

std::string Trupe::GetTitle()
{
	return title;
}

Trupe& Trupe::SetTitle(std::string ntitle)
{
	title = ntitle;
	return *this;
}

Trupe& Trupe::SetActorsAmount(int namountOfActors)
{
	amountOfActors = namountOfActors;
	return *this;
}
Trupe& Trupe::SetPayMoneyAmount(int namountOfMoney)
{
	sumMoneyForActors = namountOfMoney;
	return *this;
}

Trupe::Trupe()
{
	std::cout << "!!!! Constructor Trupe no parametrs" << std::endl;
	SetTitle("asd");
	SetActorsAmount(5);
	SetPayMoneyAmount(100);
}

Trupe::Trupe(std::string ntitle, int namountOfActors, int nsumMoneyForActors)
{
	std::cout << "!!!! Constructor Trupe with parametrs" << std::endl;
	SetTitle(ntitle);
	SetActorsAmount(namountOfActors);
	SetPayMoneyAmount(nsumMoneyForActors);
}

Trupe::Trupe(const Trupe& ntrupe)
{
	std::cout << "!!!! Copy constructor Trupe" << std::endl;
	SetTitle(ntrupe.title);
	SetActorsAmount(ntrupe.amountOfActors);
	SetPayMoneyAmount(ntrupe.sumMoneyForActors);
}

Trupe::~Trupe(){
	std::cout << "!!!! Destructor Performance" << std::endl;
}

void Trupe::ShowOnConsole()
{
	std::cout << "Title: " << title
		<< "\nAmount of actors: " << amountOfActors
		<< "\nMoney for actors: " << sumMoneyForActors << std::endl;
}