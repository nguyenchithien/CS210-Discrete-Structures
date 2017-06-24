import os

rootFolder = os.path.dirname(os.path.realpath(__file__))

directoryList = list()
fileList = list()

# Get all files and folders in this directory and subdirectories
import os

def RecursiveDirectoryWalk():
    global fileList
    global directoryList
    
    for root, directories, files in os.walk( ".", topdown = False ):
        for name in directories:
            directoryList.append( os.path.join( root, name ) )
        for name in files:
            fileList.append( os.path.join( root, name ) )

def CurrentDirectoryWalk():
    global fileList
    fileList = [ f for f in os.listdir( "." ) if os.path.isfile( f ) ]


CurrentDirectoryWalk()


for item in fileList:
    if ( ".pdf" in item ):
        # convert to png
        print( item )
        directory = item + "_slides"
        os.system( "mkdir " + directory )

        os.system( "convert -verbose -density 150 " + item + " " + directory + "/slide.png" )









