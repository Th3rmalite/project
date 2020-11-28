import invoerdefinitions as d


def setup():
    d.setupCards()
        

def draw():
    for i in range(4):
        d.drawCards(i)

def keyTyped():
    for i in range(4):
        d.textInputs[i].addText(key)