# 1.1 Tennis
# Programmed by Rachel J Morris

import pygame, sys, math
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode( ( 1024, 768 ) )
pygame.display.set_caption( "Tennis" )

bgColor = pygame.Color( 135, 215, 105 )
txtColor = pygame.Color( 0, 0, 0 )

fontObj = pygame.font.Font( "content/cnr.otf", 20 )

columnCount = 0
setCount = 0
riggsScore = 0
kingScore = 0
tennisScores = [ 0, 15, 30, 40, "game" ]
chanceOfKingWinning = 0.55
chanceOfMatch = -1

images = {
    "King" : pygame.image.load( "content/king.png" ),
    "Riggs" : pygame.image.load( "content/riggs.png" ),
    "Reset" : pygame.image.load( "content/reset.png" )
}

people = []

buttons = []
matchText = {}

winImages = []
    
def Reset():
    
    del people[:]
    del buttons[:]
    del winImages[:]
    matchText.clear()
    
    print( "Reset" )
    
    global columnCount
    global setCount
    global riggsScore
    global kingScore
    global tennisScores
    global chanceOfKingWinning
    global chanceOfMatch
    
    
    columnCount = 0
    setCount = 0
    riggsScore = 0
    kingScore = 0
    tennisScores = [ 0, 15, 30, 40, "game" ]
    chanceOfKingWinning = 0.55
    chanceOfMatch = -1
    
    global people
    global buttons
    global matchText

    people = [
        { "name" : "King",  "image" : images["King"],       "x" : 0, "y" : 50, "w" : 64, "h" : 96 },
        { "name" : "Riggs", "image" : images["Riggs"],      "x" : 0, "y" : 130, "w" : 64, "h" : 96 },
    ]

    buttons = [
        { "name" : "Reset", "image" : images["Reset"],      "x" : 800, "y" : 50, "w" : 150, "h" : 50 },
    ]

    matchText = {
        "set" : { "label" : fontObj.render( "Set 1", False, txtColor ), "pos" : ( 0, 0 ) },
        "kingscore" : { "label" : fontObj.render( "King: 0", False, txtColor), "pos" : ( 100, 0 ) },
        "riggsscore" : { "label" : fontObj.render( "Riggs: 0", False, txtColor), "pos" : ( 300, 0 ) },
        "chance" : { "label" : fontObj.render( "Chance: -", False, txtColor), "pos" : ( 500, 0 ) },
    }
    
    
def IsClicked( mouseX, mouseY, obj ):
    return ( mouseX >= obj["x"] 
            and mouseX <= obj["x"] + obj["w"]
            and mouseY >= obj["y"]
            and mouseY <= obj["y"] + obj["h"] )

def AddWinner( winner ):
    global riggsScore
    global kingScore
    global setCount
    global columnCount
    x = columnCount * 70 + 100
    y = setCount * 200 + 80
    print( "Round", columnCount, "Set", setCount )
    
    newImage = { "image" : images[ winner ], "pos" : ( x, y ) }
    
    if ( winner == "Riggs" ):
        if ( riggsScore == 3 and kingScore == 3 ):
            kingScore -= 1
        else:
            riggsScore += 1
        
    elif ( winner == "King" ):
        if ( riggsScore == 3 and kingScore == 3 ):
            riggsScore -= 1
        else:
            kingScore += 1
        
    matchText[ "riggsscore" ]["label"] = fontObj.render( "Riggs: " + str( tennisScores[ riggsScore ] ), False, txtColor )
    matchText[ "kingscore" ]["label"] = fontObj.render( "King: " + str( tennisScores[ kingScore ] ), False, txtColor )
    
    global chanceOfMatch
    global chanceOfKingWinning
    if ( chanceOfMatch == -1 ):
        if ( winner == "Riggs" ):
            chanceOfMatch = (1 - chanceOfKingWinning)
        elif ( winner == "King" ):
            chanceOfMatch = chanceOfKingWinning
    else:
        if ( winner == "Riggs" ):
            chanceOfMatch = chanceOfMatch * (1 - chanceOfKingWinning)
        else:
            chanceOfMatch = chanceOfMatch * chanceOfKingWinning
    matchText[ "chance" ]["label"] = fontObj.render( "Chance: " + str( chanceOfMatch * 100 ) + "%", False, txtColor )
        
    winImages.append( newImage )

def ClickPerson( mouseX, mouseY ):
    for person in people:
        if ( IsClicked( mouseX, mouseY, person ) ):
            print( person["name"], " wins" )
            AddWinner( person["name"] )
            return True
            
    for button in buttons:
        if ( IsClicked( mouseX, mouseY, button ) ):
            Reset()
            return False
            
def NextSet():
    print( "Next set" )
    global riggsScore
    global kingScore
    global setCount
    global columnCount
    
    setCount += 1
    kingScore = 0
    riggsScore = 0
    columnCount = 0
    people[0]["y"] += 200
    people[1]["y"] += 200
    
    matchText["set" + str(setCount)] = { "label" : fontObj.render( "Set " + str( setCount+1 ), False, txtColor ), "pos" : ( 0, setCount * 200 ) }
    matchText["riggsscore"]["pos"] = ( 100, setCount * 200 )
    matchText["kingscore"]["pos"] = ( 300, setCount * 200 )
    
    matchText[ "riggsscore" ]["label"] = fontObj.render( "Riggs: " + str( tennisScores[ riggsScore ] ), False, txtColor )
    matchText[ "kingscore" ]["label"] = fontObj.render( "King: " + str( tennisScores[ kingScore ] ), False, txtColor )
    
    chanceOfMatch = -1
    
   

Reset()
      
while True:
    window.fill( bgColor )
    
    for event in pygame.event.get():
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()
            
        elif ( event.type == MOUSEBUTTONDOWN ):
            mouseX, mouseY = event.pos
            if ( ClickPerson( mouseX, mouseY ) ):
                columnCount += 1
                
    if ( tennisScores[ riggsScore ] == "game" or tennisScores[ kingScore ] == "game" ):
        # Next set
        NextSet()
    
    for person in people:
        window.blit( person["image"], ( person["x"], person["y"] ) )
    
    for winner in winImages:
        window.blit( winner["image"], winner["pos"] )
    
    for key, text in matchText.items():
        window.blit( text["label"], text["pos"] )
    
    for button in buttons:
        window.blit( button["image"], ( button["x"], button["y"] ) )
    
    pygame.display.update()
    fpsClock.tick( 30 )
