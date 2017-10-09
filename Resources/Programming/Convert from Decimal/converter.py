# Function definition
def ConvertFromDecimal( n, b ):
    print( "" )
    print( "n = " + str( n ) + ", b = " + str( b ) )

    number = ""

    print( "" )
    while ( n > 0 ):
        q = n / b
        r = n % b

        print( str( n ) + "/" + str( b ) + " = " + str( q ) + " + " + str( r ) + "/" + str( b ) )

        number = str( r ) + number
        n = q

    return number

# Program
while( True ):
    n = input( "Enter a base-10 number to convert: " )
    b = input( "Enter a base to convert it to: " )

    result = ConvertFromDecimal( n, b )

    print( "" )
    print( "Result: " + result )

    print( "\n" )
