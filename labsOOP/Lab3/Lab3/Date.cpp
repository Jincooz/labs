#include "Date.h"
#include <iostream>
#include <ctime>
#include <string>
Date::Date() {
	std::cout << "!!!! Constructor Date no parametrs" << std::endl;
	day = 10;
	month = 4;
	year = 2022;
}
Date::Date(int new_d, int new_m, int new_y) {
	std::cout << "!!!! Constructor Date with parametrs" << std::endl;
	day = new_d;
	month = new_m;
	year = new_y;
}
Date::Date(const Date& new_date) {
	std::cout << "!!!! Copy constructor Date" << std::endl;
	day = new_date.day;
	month = new_date.month;
	year = new_date.year;
}
Date::~Date() {
	std::cout << "!!!! Destructor Date" << std::endl;
}
int Date::GetDay() {
	return day;
}
int Date::GetMonth() {
	return month;
}
int Date::GetYear() {
	return year;
}
Date& Date::SetDay(int nday) {
	if (nday <= 31 && nday >= 1)
		day = nday;
	return *this;
}
Date& Date::SetMonth(int nmonth) {
	if(nmonth <= 12 && nmonth >= 1)
		month = nmonth;
	return *this;
}
Date& Date::SetYear(int nyear) {
	if(nyear >= 0)
		year = nyear;
	return *this;
}


void Date::ShowOnConsole()
{
	std::cout << (day / 10 == 0) ? '\0' : '0' << day << '.'
		<< (month / 10 == 0) ? '\0' : '0' << month << '.'
		<< (year / 1000 == 0) ? '\0' : '0' << (year / 100 == 0) ? '\0' : '0' << (year / 10 == 0) ? '\0' : '0' << year << '\n';
}

Date Date::operator + (const Date value)
{
	return Date(this->day + value.day, this->month + value.month, this->year + value.year);		
}

std::ostream& operator<< (std::ostream &out, const Date& date)
{
	out << "Date : (" << date.day << "." << date.month << "." << date.year << ")\n";
	return out;
}

std::istream& operator>>(std::istream &in, Date& date)
{
	in >> date.day >> date.month >> date.year;
	return in;
}