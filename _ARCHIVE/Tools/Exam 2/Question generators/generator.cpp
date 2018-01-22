#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>
using namespace std;

vector<char> alphabet;

string I2S( int num )
{
    stringstream ss;
    ss << num;
    return ss.str();
}

class QuestionGenerator
{
	public:
	QuestionGenerator()
	{
		m_output.open( "questions.txt" );
	}
	
	~QuestionGenerator()
	{
		m_output.close();
	}
	
	void Output( const string& text )
	{
		m_output << text;
		cout << text;
	}
	
	void Output( char text )
	{
		m_output << text;
		cout << text;
	}
	
	void Start()
	{
		for ( int i = 0; i < m_testCount; i++ )
		{
			Output( "TEST " + I2S(i+1) + "\n\n" );
			
			CreateSetProblem();
		}
	}
	
	void CreateSetProblem()
	{
		// Generate sets
		vector<char> alphabetCopy = alphabet;
		string U;
		
		for ( int i = 0; i < 8; i++ )
		{
			char letter = alphabetCopy[ rand() % alphabetCopy.size() ];
			while ( U.find( letter ) != string::npos )
			{
				letter = alphabetCopy[ rand() % alphabetCopy.size() ];
			}
			U.push_back( letter );
		}
		
		string A;
		string B;
		string C;
		string D;
		
		for ( int i = 0; i < 5; i++ )
		{
			char letter = U[ rand() % U.size() ];
			while ( A.find( letter ) != string::npos )
			{
				letter = U[ rand() % U.size() ];
			}
			A.push_back( letter );
		}
		
		// B is not a subset of A
		for ( int i = 0; i < 2; i++ )
		{
			char letter = U[ rand() % U.size() ];
			while ( A.find( letter ) != string::npos || B.find( letter ) != string::npos )
			{
				letter = U[ rand() % U.size() ];
			}
			B.push_back( letter );
		}
		
		// C is a subset of A
		for ( int i = 0; i < 3; i++ )
		{
			C.push_back( A[i] );
		}
		
		// D is a subset of A
		for ( int i = 3; i < 5; i++ )
		{
			D.push_back( A[i] );
		}
		
		// C union D = A
		
		// OUTPUT
		
		
		// U
		sort( U.begin(), U.end() );
		Output( "U = { " );
		for ( unsigned int i = 0; i < U.size(); i++ )
		{
			if ( i != 0 ) { Output( ", " ); }
			Output( U[i] );
		}
		Output( " }" );
		Output( "\n" );
		
		// A
		sort( A.begin(), A.end() );
		Output( "A = { " );
		for ( unsigned int i = 0; i < A.size(); i++ )
		{
			if ( i != 0 ) { Output( ", " ); }
			Output( A[i] );
		}
		Output( " }" );
		Output( "\n" );
		
		// B
		sort( B.begin(), B.end() );
		Output( "B = { " );
		for ( unsigned int i = 0; i < B.size(); i++ )
		{
			if ( i != 0 ) { Output( ", " ); }
			Output( B[i] );
		}
		Output( " }" );
		Output( "\n" );
		
		// C
		sort( C.begin(), C.end() );
		Output( "C = { " );
		for ( unsigned int i = 0; i < C.size(); i++ )
		{
			if ( i != 0 ) { Output( ", " ); }
			Output( C[i] );
		}
		Output( " }" );
		Output( "\n" );
		
		// D
		sort( D.begin(), D.end() );
		Output( "D = { " );
		for ( unsigned int i = 0; i < D.size(); i++ )
		{
			if ( i != 0 ) { Output( ", " ); }
			Output( D[i] );
		}
		Output( " }" );
		Output( "\n" );
	}
	
	void SetTestCount( int num )
	{
		m_testCount = num;
	}
	
	private:
	ofstream m_output;
	int m_testCount;
};



int main()
{	
	srand( time( NULL ) );
	
	for ( int i = 0; i < 25; i++ )
	{
		alphabet.push_back( char( 97 + i ) );
	}
	
	QuestionGenerator qg;
	qg.SetTestCount( 1 );
	qg.Start();
	
	return 0;
}
