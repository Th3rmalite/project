import invoerscherm
import puntenscherm
screenSize = [1080, 720]
count = 1

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    invoerscherm.setup()
    lijstmetnamen = invoerscherm.getNames()
    puntenscherm.setup([['Dylan', 'blue'], ['Vincent', 'red']])
        
def draw():
    if not invoerscherm.d.navigationButtons[0].selected:
        invoerscherm.draw()
    else:
        puntenscherm.draw()

def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)