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
    phase = 0

    if state == "start":
        if phase == 0:
            invoerscherm.setup()
            phase = 1
        else:
            if not invoerscherm.d.navigationButtons[0].selected:
                invoerscherm.draw()
            else:
                state = "startGame"
                phase = 0
            
    elif state == "startGame":
        if phase == 0:
            rectMode(CORNER)
            textAlign(BASELINE)
            puntenscherm.setup(invoerscherm.getNames())
            phase = 1
        else:
            puntenscherm.draw()
    
    elif state == "endGame":
        pass
    
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