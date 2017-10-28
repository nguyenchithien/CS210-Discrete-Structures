import random
import sys

def GetIntersection( A, B ):
    newSet = []

    for a in A:
        for b in B:
            if ( a == b ):
                newSet.append( a )
    newSet.sort()
    
    return newSet

def GetUnion( A, B ):
    newSet = []
    
    for a in A:
        if a not in newSet:
            newSet.append( a )
            
    for b in B:
        if b not in newSet:
            newSet.append( b )

    newSet.sort()
            
    return newSet

def GetDifference( A, B ):
    newSet = []
    
    for a in A:
        if a not in B:
            newSet.append( a )

    newSet.sort()
            
    return newSet
    

sets = {}

universe = range( 1, 10 )

letter = "A"

# Generate sets
for i in range( 1, 5 ):

    nS = random.randint( 2, 5 )
    thisSet = []
    
    for e in range( nS ):
        element = random.randint( 1, 10 )
        thisSet.append( element )

    sets[ letter ] = thisSet
    letter = chr( ord( letter ) + 1 )

# Show sets
print( "U = ", universe )

for key, value in sets.iteritems():
    print( key + " = ", value )

# Do operations

print( "\n\n OPERATIONS \n" )

for k1, s1 in sets.iteritems():
    for k2, s2 in sets.iteritems():
        if k1 == k2:
            continue
            
        sys.stdout.write( k1 + " n " + k2 + ": \t\t" )
        sys.stdout.write( str( GetIntersection( sets[ k1 ], sets[ k2 ] ) ) )
        print( "" )
        sys.stdout.write( k1 + " u " + k2 + ": \t\t" )
        sys.stdout.write( str( GetUnion( sets[ k1 ], sets[ k2 ] ) ) )
        print( "" )
        sys.stdout.write( k1 + " - " + k2 + ": \t\t" )
        sys.stdout.write( str( GetDifference( sets[ k1 ], sets[ k2 ] ) ) )
        print( "" )
        sys.stdout.write( k1 + " - " + k2 + ": \t\t" )
        sys.stdout.write( str( GetDifference( sets[ k2 ], sets[ k1 ] ) ) )
        print( "" )
        sys.stdout.write( k1 + "': \t\t" )
        sys.stdout.write( str( GetDifference( universe, sets[ k1 ] ) ) )
        print( "" )
        sys.stdout.write( k2 + "': \t\t" )
        sys.stdout.write( str( GetDifference( universe, sets[ k2 ] ) ) )
        print( "" )
        print( "\n" )



