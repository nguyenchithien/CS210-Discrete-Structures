#include <iostream>
using namespace std;

int main()
{
    int numbers = 0;
    cout << "How many numbers in the sequence? ";
    cin >> numbers;
    
    int sequence[ 20 ]; // hard coded for easiness
    
    cout << "Enter the values in the sequence, separated by spaces." << endl;
    for ( int i = 0; i < numbers; i++ )
    {
        cout << "Number at index " << (i+1) << ": ";
        cin >> sequence[i];
    }
    
    cout << endl << endl << "Analysis..." << endl;
    int diff = 0, lastdiff = 0;
    for ( int i = 1; i < numbers; i++ )
    {
        diff = sequence[i] - sequence[i-1];
        cout << "a[" << i << "] = " << sequence[i] << "\t";
        cout << "a[" << i-1 << "] = " << sequence[i-1] << "\t";
        cout << "Difference: " << diff << "\t";
        if ( i != 1 ) {
            cout << "PREVIOUS DIFFERENCE + " << (diff - lastdiff);
        }
        cout << endl;
        
        lastdiff = diff;
    }
    
    return 0;
}


