#include "Repertoire.h"
#include <iostream>

std::string Repertoire::GetPlace()
{
	return place;
}

Repertoire& Repertoire::SetPlace(std::string nplace)
{
	place = nplace;
	return *this;
}

Performance* Repertoire::GetPerformances()
{
	return perfomences;
}

Repertoire& Repertoire::Add(Performance nperf)
{
	size++;
	Performance * nperfomences = new Performance[size];
	for (int i = 0; i < size - 1; i++)
	{
		nperfomences[i] = perfomences[i];
	}
	nperfomences[size - 1] = nperf;
	delete [] perfomences;
	perfomences = nperfomences;
	return *this;
}

Repertoire::~Repertoire()
{
	delete[] perfomences;
}

Repertoire::Repertoire()
{
	size = 0;
	perfomences = new Performance[size];
	place = "Ukraine";
}

Repertoire::Repertoire(std::string nplace, Performance* nperfomences, int nperfomences_size)
{
	size = nperfomences_size;
	place = nplace;
	perfomences = nperfomences;
}

Repertoire::Repertoire(const Repertoire& nrepertoire)
{
	size = nrepertoire.size;
	place = nrepertoire.place;
	perfomences = nrepertoire.perfomences;
}

void Repertoire::ShowOnConsoleLong()
{
	std::cout << "Repertoire\nPlace: " << place << "\nAmount of perfomance: " << size << std::endl;
	for (int i = 0; i < size; i++)
	{
		perfomences[i].ShowOnConsole();
	}
}

void Repertoire::ShowOnConsoleShort()
{
	std::cout << "Repertoire\nPlace: " << place << "\nAmount of perfomance: " << size << std::endl;
}