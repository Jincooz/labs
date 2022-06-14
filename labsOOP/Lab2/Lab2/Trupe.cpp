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
	SetTitle("asd");
	SetActorsAmount(5);
	SetPayMoneyAmount(100);
}

Trupe::Trupe(std::string ntitle, int namountOfActors, int nsumMoneyForActors)
{
	SetTitle(ntitle);
	SetActorsAmount(namountOfActors);
	SetPayMoneyAmount(nsumMoneyForActors);
}

Trupe::Trupe(const Trupe& ntrupe)
{
	SetTitle(ntrupe.title);
	SetActorsAmount(ntrupe.amountOfActors);
	SetPayMoneyAmount(ntrupe.sumMoneyForActors);
}

Trupe::~Trupe(){}

void Trupe::ShowOnConsole()
{
	std::cout << "Title: " << title
		<< "\nAmount of actors: " << amountOfActors
		<< "\nMoney for actors: " << sumMoneyForActors << std::endl;
}