import invoerdefinitions as d
import main

def settings():
    size(1080,720)

def setup():
    d.setupCards()
    d.setupRest()
        
def draw():
    for i in range(4):
        d.drawCards(i)
    d.drawRest()

def getNames():
    temp = []
    for i in range(len(d.players)):
        if d.players[i][1] != "None":
            temp.append([d.players[i][0], d.players[i][1]])
    return temp