import invoerscherm
import puntenscherm
import objectsScreen
screenSize = [1080, 720]
state = "objects"


def settings():
    if state == "start":
        size(screenSize[0], screenSize[1])


def setup():
    global state
    
    if state == "start":
        invoerscherm.setup()
      
        
def draw():
    global state
    
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

    elif state == "objects":
        objectsScreen.draw()
    
def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)