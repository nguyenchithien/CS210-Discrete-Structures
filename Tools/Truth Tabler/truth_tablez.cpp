#include <iostream>
#include <fstream>
using namespace std;

bool Statement( int p, int q, int r )
{
	return
		( p || q || r ) &&
		!( ( p && q ) ||
			( p && r ) ||
			( q && r ) ) &&
		!( p && q && r );
}

bool Statement2( int p, int q, int r )
{
	return
		( p && !q && !r ) || ( q && !p && !r ) || ( r && !p && !q );
}

bool Statement3( int f, int g, int c )
{
	return
		( f && g && !c ) || ( f && c && !g ) || ( g && c && !f );
}

bool Statement4( int f, int g, int c )
{
	return
		( ( f && g ) || ( f && c ) || ( g && c ) ) && ! ( f && g && c );
}

int main()
{	
	ofstream table( "table.csv" );
	
	table << "p,q,r," 
		<< "( f && g && !c ) || ( f && c && !g ) || ( g && c && !f )"
		<< endl;
	
	for ( int p = 1; p >= 0; p-- )
	{
		for ( int q = 1; q >= 0; q-- )
		{
			for ( int r = 1; r >= 0; r-- )
			{
				table << p << "," << q << "," << r << ","
					<< Statement3( p, q, r ) << endl;
			}
		}
	}
	
	table << endl;
	table << "p,q,r," 
		<< "( ( f && g ) || ( f && c ) || ( g && c ) ) && ! ( f && g && c )"
		<< endl;
	
	for ( int p = 1; p >= 0; p-- )
	{
		for ( int q = 1; q >= 0; q-- )
		{
			for ( int r = 1; r >= 0; r-- )
			{
				table << p << "," << q << "," << r << ","
					<< Statement4( p, q, r ) << endl;
			}
		}
	}
	
	
	table.close();
	
	return 0;
}
