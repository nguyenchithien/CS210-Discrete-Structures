#include <iostream>
using namespace std;

int main()
{
    // Summation from k = 1 to 5, of 2k
    
    int sum = 0;
    for ( int k = 1; k <= 5; k++ )
    {
        sum += 2 * k;
        cout << "Step " << k << " = " << sum << endl;
    }
    
    return 0;
}


