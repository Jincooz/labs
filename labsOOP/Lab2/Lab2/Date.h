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
};

