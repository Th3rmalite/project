import invoerscherm
import puntenscherm
screenSize = [1080, 720]
count = 1
state = "start"


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
        rectMode(LEFT)
        #puntenscherm.setup(invoerscherm.getNames())
        puntenscherm.setup([("Vincent","black"),("beide Dylans","white"),("beide Dylans","red"),("beide Dylans","blue")])
        state = "startGame"
        
    elif state == "startGame":
        puntenscherm.draw()
    
    
def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)