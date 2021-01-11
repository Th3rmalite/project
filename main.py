import invoerscherm
import puntenscherm
import eindscherm
screenSize = [1080, 720]
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
        rectMode(CORNER)
        textAlign(BASELINE)
        puntenscherm.setup(invoerscherm.getNames())
        state = "startGame"
        
    elif state == "startGame":
        puntenscherm.draw()
        if len(puntenscherm.dp.getAlivePlayers()) == 1:
            state = "endGameSetup"
    
    elif state == "endGameSetup":
        eindscherm.setup()
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