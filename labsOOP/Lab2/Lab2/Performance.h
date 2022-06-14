#include <string>
#include "Apartment.h"
#include "Trupe.h"
#include "Date.h"
#pragma once

enum class Category {
	Drama,
	Operetta,
	Opera,
	Ballet
};

class Performance
{
private:
	std::string title;
	Category category;
	Apartment apartament;
	Trupe trupe;
	Date perfomanceDate;
	int orendPrice;
	bool needOrchestr;
public:
	Performance();
	Performance(	std::string ntitle, 
					Category ncategory,
					Apartment napartament,
					Trupe ntrupe,
					Date nperfomanceDate,
					int norendPrice,
					bool nneedOrchestr);
	Performance(const Performance& napartment);
	~Performance();
	std::string GetTitle();
	Category GetCategory();
	Apartment GetApartament();
	Trupe GetTrupe();
	Date GetDate();
	int GetOrendPrice();
	bool GetHaveOrchestr();

	Performance& SetTitle(std::string ntitle);
	Performance& SetCategory(Category ncategory);
	Performance& SetApartament(Apartment napartment);
	Performance& SetTrupe(Trupe ntrupe);
	Performance& SetDate(Date ndate);
	Performance& SetOrendPrice(int norendPrice);
	Performance& SetHaveOrchestr(bool nneedOrchestr);

	void ShowOnConsole();
};

