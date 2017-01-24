# 1.1 Magic Trick Illustration
# Programmed by Rachel J Morris

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode( ( 1024, 768 ) )
pygame.display.set_caption( "Magic Trick" )

bgColor = pygame.Color( 140, 225, 255 )
txtColor = pygame.Color( 0, 0, 0 )

fontObj = pygame.font.Font( "content/cnr.otf", 32 )
lblTop = fontObj.render( "Top", False, txtColor )
lblTopPos = ( 800, 20 )
lblBottom = fontObj.render( "Bottom", False, txtColor )
lblBottomPos = ( 50, 20 )

cardImages = {
    "heart" : pygame.image.load( "content/heartcard.png" ),
    "club" : pygame.image.load( "content/clubcard.png" ),
    "diamond" : pygame.image.load( "content/diamondcard.png" ),
    "spade" : pygame.image.load( "content/spadecard.png" ),
    "back" : pygame.image.load( "content/cardback.png" )
}

cards = [
    { "name" : "heart",     "faceup" : True,    "x" : 50,     "y" : 50,     "w" : 100,  "h" : 125,    "image" : cardImages["heart"] },
    { "name" : "club",      "faceup" : True,    "x" : 300,    "y" : 50,     "w" : 100,  "h" : 125,    "image" : cardImages["club"] },
    { "name" : "diamond",   "faceup" : True,    "x" : 550,    "y" : 50,     "w" : 100,  "h" : 125,    "image" : cardImages["diamond"] },
    { "name" : "spade",     "faceup" : True,    "x" : 800,    "y" : 50,     "w" : 100,  "h" : 125,    "image" : cardImages["spade"] }
]

def IsCardClicked( card ):
    return ( mouseX >= card["x"] 
            and mouseX <= card["x"] + card["w"]
            and mouseY >= card["y"]
            and mouseY <= card["y"] + card["h"] )
    
def FlipCard( mouseX, mouseY ):
    for card in cards:
        if ( IsCardClicked( card ) ):
                # flip it
                card["faceup"] = not card["faceup"]
                if ( card["faceup"] ):
                    card["image"] = cardImages[ card["name"]]
                else:
                    card["image"] = cardImages["back"]

def MoveCard( mouseX, mouseY, card ):
    # Offset so that moving based on center of card
    card["x"] = mouseX - card["w"] / 2
    card["y"] = mouseY - card["h"] / 2

mouseDown = False
movingCard = None

while True:
    window.fill( bgColor )
    
    for event in pygame.event.get():
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()
            
        elif ( event.type == MOUSEMOTION ):
            mouseX, mouseY = event.pos
            
            if ( mouseDown and movingCard != None ):
                MoveCard( mouseX, mouseY, movingCard )
            
        elif ( event.type == MOUSEBUTTONDOWN ):
            mouseDown = True
            for card in cards:
                if ( IsCardClicked( card ) ):
                    movingCard = card
                    print( "Move card:", movingCard["name"] )
            
        elif ( event.type == MOUSEBUTTONUP ):
            mouseX, mouseY = event.pos
            mouseDown = False
            movingCard = None
            
            if ( event.button == 3 ):
                FlipCard( mouseX, mouseY )
    
    for card in cards:
        window.blit( card["image"], ( card["x"], card["y"] ) )
            
    window.blit( lblTop, lblTopPos )
    window.blit( lblBottom, lblBottomPos )
    
    pygame.display.update()
    fpsClock.tick( 30 )
