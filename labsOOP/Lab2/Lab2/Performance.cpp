#include "Performance.h"
#include <iostream>


std::string Performance::GetTitle()
{
	return title;
}
Category Performance::GetCategory()
{
	return category;
}
Apartment Performance::GetApartament()
{
	return apartament;
}
Trupe Performance::GetTrupe()
{
	return trupe;
}
Date Performance::GetDate()
{
	return perfomanceDate;
}
int Performance::GetOrendPrice()
{
	return orendPrice;
}
bool Performance::GetHaveOrchestr()
{
	return needOrchestr;
}

Performance& Performance::SetTitle(std::string ntitle)
{
	title = ntitle;
	return *this;
}
Performance& Performance::SetCategory(Category ncategory)
{
	category = ncategory;
	return *this;
}
Performance& Performance::SetApartament(Apartment napartment)
{
	apartament = napartment;
	return *this;
}
Performance& Performance::SetTrupe(Trupe ntrupe)
{
	trupe = ntrupe;
	return *this;
}
Performance& Performance::SetDate(Date ndate)
{
	perfomanceDate = ndate;
	return *this;
}
Performance& Performance::SetOrendPrice(int norendPrice)
{
	orendPrice = norendPrice;
	return *this;
}
Performance& Performance::SetHaveOrchestr(bool nneedOrchestr)
{
	needOrchestr = nneedOrchestr;
	return *this;
}

Performance::Performance()
{
	SetTitle("Swan Lake")
	.SetCategory(Category::Ballet)
	.SetOrendPrice(1000)
	.SetHaveOrchestr(false);
}
Performance::Performance(std::string ntitle,
	Category ncategory,
	Apartment napartament,
	Trupe ntrupe,
	Date nperfomanceDate,
	int norendPrice,
	bool nneedOrchestr)
{
	SetTitle(ntitle)
		.SetCategory(ncategory)
		.SetApartament(napartament)
		.SetTrupe(ntrupe)
		.SetDate(nperfomanceDate)
		.SetOrendPrice(norendPrice)
		.SetHaveOrchestr(nneedOrchestr);
}
Performance::Performance(const Performance& napartment)
{
	SetTitle(napartment.title)
		.SetCategory(napartment.category)
		.SetApartament(napartment.apartament)
		.SetTrupe(napartment.trupe)
		.SetDate(napartment.perfomanceDate)
		.SetOrendPrice(napartment.orendPrice)
		.SetHaveOrchestr(napartment.needOrchestr);
}
Performance::~Performance() {}
void Performance::ShowOnConsole()
{
	std::cout << "Title: " << title << "\nCategory: ";
	switch (category)
	{
	case Category::Drama:
	{
		std::cout << "Drama\n";
		break;
	}
	case Category::Ballet:
	{
		std::cout << "Ballet\n";
		break;
	}
	case Category::Opera:
	{
		std::cout << "Opera\n";
		break;
	}
	case Category::Operetta:
	{
		std::cout << "Operetta\n";
		break;
	}
	default:
		break;
	}
	apartament.ShowOnConsole();
	trupe.ShowOnConsole();
	perfomanceDate.ShowOnConsole();
	std::cout << "Orend price: " << orendPrice
		<< "\nOrchestr " << (needOrchestr ? " need\n" : "no need\n");
}