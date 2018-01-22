#include <iostream>
#include <string>
#include <vector>
using namespace std;

void DisplaySet( string setname, vector<string> set )
{
	cout << setname << " = { ";
	
	for ( unsigned int i = 0; i < set.size(); i++ )
	{
		if ( i != 0 ) { cout << ", "; }
		cout << set[i];
	}
	cout << " }" << endl;
}

vector<string> CartesianProduct( const vector<string>& A, const vector<string>& B )
{
	vector<string> C;
	
	for ( unsigned int x = 0; x < A.size(); x++ )
	{
		for ( unsigned int y = 0; y < B.size(); y++ )
		{
			string pair = "(" + A[x] + ", " + B[y] + ")";
			
			C.push_back( pair );
		}
	}
	
	return C;
}

int main()
{
	vector<string> B = { "3", "6", "9" };
	vector<string> A = { "3", "6" };
	vector<string> C;
	
	DisplaySet( "A", A );
	DisplaySet( "B", B );
	
	C = CartesianProduct( A, B );
	
	cout << "A x B = C" << endl;
	
	DisplaySet( "C", C );
	
	return 0;
}
