#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    for ( int n = 1; n <= 20; n++ )
    {
        int term = pow( 2, n ) - 1;
        cout << "term " << n << " = " << term << endl;
    }
    
    return 0;
}


