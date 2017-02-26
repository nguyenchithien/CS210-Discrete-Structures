#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

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
		m_output << text << endl;
		cout << text << endl;
	}
	
	void Start()
	{
		for ( int i = 0; i < m_testCount; i++ )
		{
			Output( "TEST " + I2S(i+1) );
			Output( "\nChapter 1.2" );
			
			CreateClosedFormula();
			CreateRecursiveFormula();
			CreateSummation();
			
			Output( "\nChapter 1.3" );
			
			CreateTruthTableQuestion();
			
			Output( "\nChapter 1.4" );
			Output( "\nChapter 1.5" );
			Output( "-----------------------------------" );
			Output( "\n" );
		}
	}
	
	void CreateClosedFormula()
	{
		// a[n] = mn + b
		int m = (rand() % 3) + 1;
		int b = (rand() % 3) + 1;
		
		
		Output( "\n\t Closed formula question" );
		Output( "\t\t a[n] = " + I2S( m ) + "n + " + I2S( b ) );
		
		string sequence = "\t\t Sequence: ";
		
		for ( int i = 1; i <= 5; i++ )
		{
			if ( i != 1 ) { sequence += ", "; }
			sequence += I2S( ( m * i ) + b );
		}
		sequence += "\n";
		
		Output( sequence );
	}
	
	void CreateRecursiveFormula()
	{
		// a[1] = x
		// a[n] = m * a[n-1] + b
		int firstVal = (rand () % 2) + 1;
		int m = 2;//(rand() % 2) + 2;
		int b = (rand() % 4) + 1;
		
		Output( "\n\t Recursive formula question" );
		Output( "\t\t a[1] = " + I2S( firstVal ) );
		Output( "\t\t a[n] = " + I2S( m ) + "a[n-1] + " + I2S( b ) );
		
		string sequence = "\t\t Sequence: " + I2S( firstVal );
		
		int previousVal = firstVal;
		for ( int i = 2; i <= 5; i++ )
		{
			int newVal = m * previousVal + b;
			sequence += ", " + I2S( newVal );
			previousVal = newVal;
		}
		sequence += "\n";
		
		Output( sequence );
	}
	
	void CreateSummation()
	{
		// sum from 1 to n of a[k]
		int begin = 1;
		int end = 5;
		
		int m = (rand() % 3) + 2;
		int b = (rand() % 3) + 1;
		
		Output( "\n\t Summation question" );
		Output( "\t\t Sum from k = " 
			+ I2S( begin ) + " to " 
			+ I2S( end ) + " of "
			+ I2S( m ) + "k + " + I2S( b ) );
			
		string result = "\t\t Result: ";
		
		int sum = 0;
		for ( int k = begin; k <= end; k++ )
		{
			if ( k != begin ) { result += " + "; }
			sum += m * k + b;
			result += I2S( m * k + b );
		}		
		result += "\n";
		
		Output( result );
	}
	
	void CreateTruthTableQuestion()
	{
		Output( "\n\t Truth table question" );
		Output( "\t\t p \tq \tr \t(p && q)||(r && !q)" );
		//( q and neg p ) or ( r and neg p )
		for ( int r = 0; r <= 1; r++ )
		{
			for ( int q = 0; q <= 1; q++ )
			{
				for ( int p = 0; p <= 1; p++ )
				{
					Output( "\t\t " 
						+ I2S( p ) + "\t" 
						+ I2S( q ) + "\t" 
						+ I2S( r ) + "\t"
						+ I2S( (p && q)||(r && !q) ) );
				}
			}
		}
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
	
	QuestionGenerator qg;
	qg.SetTestCount( 1 );
	qg.Start();
	
	return 0;
}
