#include <string>
#pragma once
class Trupe
{
private:
	std::string title;
	int amountOfActors;
	int sumMoneyForActors;
public:
	Trupe();
	Trupe(std::string ntitle, int namountOfActors, int nsumMoneyForActors);
	Trupe(const Trupe& ntrupe);
	~Trupe();

	std::string GetTitle();
	int GetActorsAmount();
	int GetPayMoneyAmount();

	Trupe& SetTitle(std::string ntitle);
	Trupe& SetActorsAmount(int namountOfActors);
	Trupe& SetPayMoneyAmount(int namountOfMoney);

	void ShowOnConsole();
};

