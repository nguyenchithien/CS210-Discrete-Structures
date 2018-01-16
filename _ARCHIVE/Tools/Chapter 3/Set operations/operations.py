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
    
def OutputSet( fileHandler, key, values ):
    # So I can use it in LaTeX

    adjustKey = key.replace( "n", "\cap" ).replace( "u", "\cup" )
    
    fileHandler.write( "$" + adjustKey + " = \{ " )
    
    items = 0
    for v in values:
        if items != 0:
            fileHandler.write( ", " )

        fileHandler.write( str( v ) )
        items = items + 1

    fileHandler.write( " \}$" )
    fileHandler.write( "\n" )
        

fileHandler = open( "Sets.txt", "w" )

sets = {}

universe = range( 1, 11 )

letter = "A"

# Generate sets
for i in range( 1, 5 ):

    nS = random.randint( 2, 5 )
    thisSet = []
    
    for e in range( nS ):
        element = random.randint( 1, 10 )
        if element not in thisSet:
            thisSet.append( element )

    thisSet.sort()
    sets[ letter ] = thisSet
    letter = chr( ord( letter ) + 1 )

# Show sets
print( "U = ", universe )
OutputSet( fileHandler, "U", universe )

for key, value in sets.iteritems():
    print( key + " = ", value )
    OutputSet( fileHandler, key, value )

# Do operations
operations = {}

print( "\n\n BASIC OPERATIONS \n" )
fileHandler.write( "\n\n ------------------------------------------------------------------" )
fileHandler.write( "\n BASIC OPERATIONS \n" )

for k1, s1 in sets.iteritems():
    for k2, s2 in sets.iteritems():
        if k1 == k2:
            continue

        operationSet = {}
    
        operationSet[ k1 + " n " + k2 ] = GetIntersection( sets[ k1 ], sets[ k2 ] )
        operationSet[ k1 + " u " + k2 ] = GetUnion( sets[ k1 ], sets[ k2 ] )
        operationSet[ k1 + " - " + k2 ] = GetDifference( sets[ k1 ], sets[ k2 ] )
        operationSet[ k2 + " - " + k1 ] = GetDifference( sets[ k2 ], sets[ k1 ] )
        operationSet[ k1 + "'" ] = GetDifference( universe, sets[ k1 ] )
        operationSet[ k2 + "'" ] = GetDifference( universe, sets[ k2 ] )

        for k, o in operationSet.iteritems():
            sys.stdout.write( k + "\t" )
            sys.stdout.write( str( o ) + "\n" )
            
            OutputSet( fileHandler, k, o )
            
            operations[ k ] = o
        
        print( "\n" )
        fileHandler.write( "\n" )


print( "\n\n COMPOUND OPERATIONS \n" )

fileHandler.write( "\n\n ------------------------------------------------------------------" )
fileHandler.write( "\n COMPOUND OPERATIONS \n" )

for k1, s1 in operations.iteritems():
    for k2, s2 in operations.iteritems():
        if k1 == k2:
            continue

        operationSet = {}
    
        operationSet[ "(" + k1 + ") n (" + k2 + ")" ] = GetIntersection( s1, s2 )
        operationSet[ "(" + k1 + ") u (" + k2 + ")" ] = GetUnion( s1, s2 )
        operationSet[ "(" + k1 + ") - (" + k2 + ")" ] = GetDifference( s1, s2 )
        operationSet[ "(" + k2 + ") - (" + k1 + ")" ] = GetDifference( s2, s1 )
        operationSet[ "(" + k1 + ")'" ] = GetDifference( universe, s1 )
        operationSet[ "(" + k2 + ")'" ] = GetDifference( universe, s2 )

        for k, o in operationSet.iteritems():
            #sys.stdout.write( k + "\t" )
            #sys.stdout.write( str( o ) + "\n" )
            
            OutputSet( fileHandler, k, o )
        
        #print( "\n" )
        fileHandler.write( "\n" )
