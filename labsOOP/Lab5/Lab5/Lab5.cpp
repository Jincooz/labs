#include <windows.h>
#include <conio.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef map<string, vector<string>>::iterator bookIterator;

class Repos {
private:
	map<string, vector<string>> books; 
public:
	 Repos() {};
	 vector<string> findByAuthor(const string& author);
	 string findByName(const string& book);
	 ~Repos() {};
	 friend istream& operator>>(istream& in, Repos& value);
	 friend ostream& operator<<(ostream& out, Repos& value);
	 bool operator()(const string author, const string book);
	 bool operator()(const string author);
};


bool Repos::operator()(const string author, const string book) 
{
	bookIterator authorArray = books.find(author);
	if (authorArray != books.end()) {
	vector<string>&ptr = authorArray->second;
	if (find(ptr.begin(), ptr.end(), book) == ptr.end())
		ptr.push_back(book);
	else
		return false;
	}
	else 
	{
		books[author] = vector<string>{ book };		
	}
	return true;
}

istream& operator>>(istream& in, Repos& value) {
	 string author, book;
	 cout << "Book title: ";
	 in.ignore();
	 getline(in, book);
	 cout << "Book autor name: ";
	 getline(in, author);
	 if (value(author, book) == true)
		 cout << "Book added" << endl;
	 else
		 cout << "Book already in library" << endl;
	 return in;	
}

ostream & operator<<(ostream & out, Repos & value) {
	if (value.books.empty() == true)
		out << "Lib empty" << endl;
	else
		for (bookIterator authorBooks = value.books.begin(); authorBooks != value.books.end(); authorBooks++) 
		{
			vector<string> copy = authorBooks->second;
			sort(copy.begin(), copy.end());
			vector<string>::iterator bookIter = copy.begin();
			out << "Autor books " << authorBooks->first << " :\n" << *(bookIter++);
			for (bookIter; bookIter != copy.end(); bookIter++)
				out << "\n" << *bookIter;
			out << endl;
		}
	return out;
}

bool Repos::operator()(const string author) {
	 bookIterator authorArray = books.find(author);
	if (authorArray != books.end())
	{
		books.erase(authorArray);
		return true;	
	}
	else
		return false;
}

vector<string> Repos::findByAuthor(const string & author) {
	bookIterator authorArray = books.find(author);
	if (authorArray != books.end()) 
	{
		vector<string> copy = authorArray->second;
		sort(copy.begin(), copy.end());
		return copy;
	}
	else
	{
		 return vector<string>(0);
	}
}


string Repos::findByName(const string & book) {
	for (bookIterator ReposIterator = books.begin(); ReposIterator!= books.end(); ReposIterator++) {
		 vector<string>&ptr = ReposIterator->second;
		 vector<string>::iterator bookFound = find(ptr.begin(), ptr.end(), book);
		 if (bookFound != ptr.end())
			 return ReposIterator->first;
	}	
}

void FindBookAutor(Repos lib)
{
	string author, book;
	cout << "Book name: ";
	cin.ignore();
	getline(cin, book);
	try {
		author = lib.findByName(book);
		cout << "Book autor - " << author << endl << endl;
	}
	catch (exception)
	{
		cout << "No book in lib" << endl << endl;
	}
}

void FindBookByAutor(Repos lib)
{
	string author, book;
	vector<string> books;
	vector<string>::iterator bookIterator;
	cout << "Autor: ";
	cin.ignore();
	getline(cin, author);
	books = lib.findByAuthor(author);
	if (books.empty() == true)
		cout << "No this autor book in lib" << endl
		<< endl;
	else {
		bookIterator = books.begin();
		cout << "Book - " << *(bookIterator++);
		for (bookIterator; bookIterator != books.end();
			bookIterator++)
			cout << ", " << *bookIterator;
		cout << endl << endl;

	}
}

int main() {
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	Repos lib;
	while (true) {
		 system("cls");
		 cout	<< "1. See books" << endl
				<< "2. Add book" << endl 
				<< "3. Find book autor" << endl
				<< "4. Find book by autor" << endl 
				<< "5. Delete autor book" << endl
				<< "6. Exit" << endl;

		 cout << "Number: ";
		 int i;
		 cin >> i;
		 cout << endl;
		 switch (i) {
		 case 1:
			 cout << lib;
			 break;
		 case 2:
			 cin >> lib;
			 cout;
			 break;
		 case 3:
			 FindBookAutor(lib);
			 break;
		 case 4:
			 FindBookByAutor(lib);
			 break;
		 case 5:
		 {
			 string author;
			 cout << "Autor: ";
			 cin.ignore();
			 getline(cin, author);
			 if (lib(author) == true)
				 cout << "Books deleted";
			 else
				 cout << "No this autor book in lib";
			 break;
		 }
		 case 6:
			 return 0;
		 default:
			 break;
			
		}
		_getch();		
	}
	return 0;	
}