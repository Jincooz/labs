#include <iostream>
#pragma once
class Date
{
private:
	int year;
	int month;
	int day;
public:
	Date();
	Date(int day, int month, int year);
	Date(const Date& date);
	~Date();

	int GetYear();
	int GetMonth();
	int GetDay();

	Date& SetDay(int nday);
	Date& SetMonth(int nmonth);
	Date& SetYear(int nyear);

	void ShowOnConsole();

	Date operator + (const Date value);
	friend std::ostream& operator<< (std::ostream &out, const Date& date);
	friend std::istream& operator>> (std::istream &in, Date& date);
};

