#include <iostream>
#include <string>
using namespace std;

string DecToBinary( int n )
{
	string binary = "";
	
	while ( n > 0 )
	{
		int q, r;
		q = n / 2;
		r = n % 2;
		
		binary = to_string( r ) + binary;
		n = q;
	}
	
	return binary;
}

int main()
{
	while ( true )
	{
		cout << "Enter a number to convert to binary: ";
		int number;
		cin >> number;
		
		string binary = DecToBinary( number );
		cout << "BINARY: " << binary << endl << endl;
	}
	
	return 0;
}
