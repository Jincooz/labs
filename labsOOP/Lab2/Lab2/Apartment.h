#include <string>
#pragma once
class Apartment
{
private:
	std::string title;
	std::string address;
	int orendSum;
	int amountOfSeats;
public:
	Apartment();
	Apartment(std::string ntitle, std::string naddress, int norendSum, int namountOfSeats);
	Apartment(const Apartment& napartment);
	~Apartment();
	static int orchesterPrice;
	std::string GetTitle();
	std::string GetAddress();
	int GetOrendSum();
	int GetAmountOfSeats();

	Apartment& SetTitle(std::string ntitle);
	Apartment& SetAddress(std::string naddress);
	Apartment& SetOrendSum(int norendSum);
	Apartment& SetAmountOfSeats(int namountOfSeats);

	void ShowOnConsole();
};



