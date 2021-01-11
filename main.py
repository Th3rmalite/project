import invoerscherm
import puntenscherm
import eindscherm
from objects import *
screenSize = [1080, 720]
state = "start"


def settings():
    if state == "start":
        size(screenSize[0], screenSize[1])


def setup():
    global state, background
    
    if state == "start":
        invoerscherm.setup()
    
    main = Screen(None, {})
    main.start()
    background = Rectangle(None, {
        'fill': '245 245 245 255',
        'w': '1080',
        'h': '720'
    })
    main.stop()
      
        
def draw():
    global state
    background.draw()
    
    if state == "start":
        invoerscherm.draw()
        if not invoerscherm.d.navigationButtons[0].selected:
            invoerscherm.draw()
        else:
            state = "createGame"
            
    elif state == "createGame":
        rectMode(CORNER)
        textAlign(BASELINE)
        puntenscherm.setup(invoerscherm.getNames())
        state = "startGame"
        
    elif state == "startGame":
        puntenscherm.draw()
        if type(puntenscherm.dp.getAlivePlayers()) != type(0):
            if len(puntenscherm.dp.getAlivePlayers()) == 1:
                puntenscherm.toEnd.draw()
        else:
            if puntenscherm.dp.getAlivePlayers() == 1:
                puntenscherm.toEnd.draw()
        if puntenscherm.toEnd.isSelected:
            state = "endGameSetup"
        font = loadFont('OpenSans-48.vlw')
        textFont(font, 16)
        
                
        puntenscherm.dp.getPlayers()
    
    elif state == "endGameSetup":	
        noTint()
        eindscherm.setup(puntenscherm.dp.getPlayers())
        cursor(ARROW)
        state = "endGame"
    elif state == "endGame":
        eindscherm.draw()
    
def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)

    if key == TAB:
        textInputs = invoerscherm.d.textInputs
        for i in range(len(textInputs)):
            if textInputs[i].selected == True:
                textInputs[i].selected = False
                textInputs[i].defineText()
                if i + 1 > 3:
                    textInputs[0].selected = True
                else:
                    textInputs[i + 1].selected = True
                break