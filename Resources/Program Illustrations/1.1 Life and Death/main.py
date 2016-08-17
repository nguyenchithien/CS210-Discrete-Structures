# 1.1 Life and Death
# Programmed by Rachel J Morris

import pygame, sys, math
from pygame.locals import *

maximumPeople = input( "HOW MANY PEOPLE SHOULD BE IN A CIRCLE? " )

pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode( ( 768, 768 ) )
pygame.display.set_caption( "Magic Trick" )

bgColor = pygame.Color( 140, 225, 255 )
txtColor = pygame.Color( 0, 0, 0 )

fontObj = pygame.font.Font( "content/cnr.otf", 20 )

people = []
#maximumPeople = 29

circleRatio = 360 / maximumPeople
index = 0
w = 64
h = 96
radius = 300
offsetY = 350

for index in range( maximumPeople ):
    x = math.cos( math.radians( circleRatio * index ) ) * radius + offsetY
    y = math.sin( math.radians( circleRatio * index ) ) * radius + offsetY
    
    imgNum = ( index % 16 ) + 1
    
    txtObj = fontObj.render( str( index+1 ), False, txtColor )
    person = { "number" : index, "alive" : True, 
        "x" : x, "y" : y, "w" : 64, "h" : 96,
        "image" : pygame.image.load( "content/" + str( imgNum ) + ".png" ), "label" : txtObj, 
        "labelpos" : ( x, y ) }
    people.append( person )
    
    print( "Person ", index, circleRatio * index, " = ", x, ", ", y )
    
    index += 1
    
def IsClicked( mouseX, mouseY, obj ):
    return ( mouseX >= obj["x"] 
            and mouseX <= obj["x"] + obj["w"]
            and mouseY >= obj["y"]
            and mouseY <= obj["y"] + obj["h"] )

def ClickPerson( mouseX, mouseY ):
    for person in people:
        if ( IsClicked( mouseX, mouseY, person ) ):
            person["alive"] = not person["alive"]
            print( "Person ", person["number"], person["alive"] )
            
            if ( person["alive"] ):
                print( "Alive" )
                person["image"] = pygame.transform.rotate( person["image"], 90 )
                
            else:
                person["image"] = pygame.transform.rotate( person["image"], -90 )

while True:
    window.fill( bgColor )
    
    for event in pygame.event.get():
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()
            
        elif ( event.type == MOUSEBUTTONDOWN ):
            mouseX, mouseY = event.pos
            ClickPerson( mouseX, mouseY )
            
        elif ( event.type == MOUSEBUTTONUP ):
            mouseX, mouseY = event.pos
    
    for person in people:
        window.blit( person["image"], ( person["x"], person["y"] ) )
        window.blit( person["label"], person["labelpos"] )
        
    #window.blit( lblBottom, lblBottomPos )
    
    pygame.display.update()
    fpsClock.tick( 30 )
