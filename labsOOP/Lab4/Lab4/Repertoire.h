#pragma once
#include <string>
#include "Performance.h"
class Repertoire
{
private:
	std::string place;
	Performance* perfomences;
	int size;
public:
	std::string GetPlace();
	Repertoire& SetPlace(std::string newPlace);
	Performance* GetPerformances();
	Repertoire& Add(Performance nperf);
	Repertoire();
	Repertoire(std::string nplace, Performance* nperfomences, int nperfomences_size);
	Repertoire(const Repertoire& nrepertoire);
	~Repertoire();
	void ShowOnConsoleLong();
	void ShowOnConsoleShort();

	Performance& operator[] (const int index);
};