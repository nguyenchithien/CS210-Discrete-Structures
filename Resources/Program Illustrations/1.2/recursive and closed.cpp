#include <iostream>
using namespace std;

void DisplayList( int sequence[5] );

int main()
{
    // Describe the sequence 1, 3, 5, 7, 9, ...
    // in terms of Closed and Recursive
    
    int closedSequence[5];    
    
    for ( int i = 0; i < 5; i++ )
    {
        int n = i + 1;
        closedSequence[i] = ( 2 * n ) - 1;
    }
    
    DisplayList( closedSequence );
    
    
    // Recursive sequence
    int recSequence[5];
    recSequence[0] = 1;
    for ( int n = 1; n < 5; n++ )
    {
        recSequence[n] = recSequence[n-1] + 2;
    }
    
    DisplayList( recSequence );
   
    return 0;
}



void DisplayList( int sequence[5] )
{
    for ( int n = 0; n < 5; n++ ) 
    {
        cout << "Index " << n << " = " << sequence[n] << endl;
    }
}
