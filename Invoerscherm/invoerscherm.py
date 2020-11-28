import invoerdefinitions as d

def setup():
    size(d.screenSize[0], d.screenSize[1])
    d.setupCards()
        

def draw():
    for i in range(4):
        d.drawCards(i)

def keyTyped():
    for i in range(4):
        d.textInputs[i].addText(key)