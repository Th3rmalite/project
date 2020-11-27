import invoerdefinitions as d

def setup():
    global screenSize
    global Card
    global TextInput
    global ColorPicker
    size(d.screenSize[0], d.screenSize[1])
    background(color(d.palette['dark_gray']))
    textSize(16)
    for i in range(4):
        d.cards.append(d.Card(i, d.screenSize[0]/2, 160, 400, 110, 10, 'solid_white'))
        d.colorPickers.append(d.ColorPicker(i, d.cards[i].x, d.cards[i].y, 30, 35))
        d.textInputs.append(d.TextInput(i,d.cards[i].x,d.cards[i].y, 200))
        d.cards[i].shadow(6, 1, 1)
        d.players.append(['Name','Color',d.cards[i],d.colorPickers[i]])
        

def draw():
    for i in range(4):
        d.drawCards(i)

def keyTyped():
    for i in range(4):
        d.textInputs[i].addText(key)