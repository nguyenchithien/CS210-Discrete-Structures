#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string trueFalse[] = { "F", "T" };

bool Question5a( int p, int q, int r )
{
	return
		(p || q) && r;
}

bool Question5b( int p, int q, int r )
{
	return
		(p && q) || (p && r);
}

bool Question5c( int p, int q, int r )
{
	return
		(p && q && r) || ((p && !q && !r) || (!p && q && !r) || (!p && !q && r));
}

int main()
{	
	ofstream table( "table.csv" );
	
	table << "Question 5a" << endl;
	
	table << ",p,q,r,|,student answer" << endl;
	
	for ( int p = 1; p >= 0; p-- )
	{
		for ( int q = 1; q >= 0; q-- )
		{
			for ( int r = 1; r >= 0; r-- )
			{
				table << "," << trueFalse[p] << "," << trueFalse[q] << "," << trueFalse[r] << "," << "|,"
					<< trueFalse[ Question5a( p, q, r ) ] << endl;
			}
		}
	}
	
	table << "Question 5b" << endl;
	table << ",p,q,r,|,student answer" << endl;
	
	for ( int p = 1; p >= 0; p-- )
	{
		for ( int q = 1; q >= 0; q-- )
		{
			for ( int r = 1; r >= 0; r-- )
			{
				table << "," << trueFalse[p] << "," << trueFalse[q] << "," << trueFalse[r] << "," << "|,"
					<< trueFalse[ Question5b( p, q, r ) ] << endl;
			}
		}
	}
	
	table << "Question 5c" << endl;
	table << ",p,q,r,|,student answer" << endl;
	
	for ( int p = 1; p >= 0; p-- )
	{
		for ( int q = 1; q >= 0; q-- )
		{
			for ( int r = 1; r >= 0; r-- )
			{
				table << "," << trueFalse[p] << "," << trueFalse[q] << "," << trueFalse[r] << "," << "|,"
					<< trueFalse[ Question5c( p, q, r ) ] << endl;
			}
		}
	}
	
	
	table.close();
	
	return 0;
}
