import invoerdefinitions as d
import main
from objects import *

def settings():
    size(1080,720)

def setup():
    global invoerScherm, toNext
    invoerScherm = Screen('invoerScherm', {})
    invoerScherm.start()

    background = Rectangle(None, {
        'fill': '245 245 245 255',
        'w': '1080',
        'h': '720'
    })
    invoerScherm.stop()
    d.setupCards()
    d.setupRest()
        
def draw():
    for i in range(len(invoerScherm.content)):
        invoerScherm.content[i].draw()
        font = loadFont('OpenSans-48.vlw')
        textFont(font, 16)
    rectMode(CENTER)
    for i in range(4):
        d.drawCards(i)
    d.drawRest()

def getNames():
    temp = []
    for i in range(len(d.players)):
        if d.players[i][1] != "None":
            temp.append([d.players[i][0], d.players[i][1]])
    return temp