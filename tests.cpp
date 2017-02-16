float GetArea( float width, float height )
{
	return 2 * width + 2 * height;
}

void Test_GetArea()
{
	// Test 1
	if ( GetArea( 2, 3 ) != 6 )
	{
		cout << "Test 1 failed!" << endl;
	}
	
	// Test 2
	if ( GetArea( 10, 5 ) != 50 )
	{
		cout << "Test 2 failed!" << endl;
	}
}