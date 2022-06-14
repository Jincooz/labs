#include "Date.h"
#include <iostream>
#include <ctime>
#include <string>
Date::Date() {
	day = 10;
	month = 4;
	year = 2022;
}
Date::Date(int new_d, int new_m, int new_y) {
	day = new_d;
	month = new_m;
	year = new_y;
}
Date::Date(const Date& new_date) {
	day = new_date.day;
	month = new_date.month;
	year = new_date.year;
}
Date::~Date() {
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