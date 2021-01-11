import invoerdefinitions as d
from objects import *
import drawPlayers as dp

def setup(playerList):
    global invoerScherm
    dp.get_players(playerList)
    invoerScherm = Screen('namen', {})
    invoerScherm.start()
    toEnd = Button(None, {
        'x': 980,
        'y': 670,
        'w': 130,
        'h': 50,
        'stroke': 'None',
        'fill': '138 201 38 255',
        'placeholder': 'Einde spel',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER]
    })
    toEnd.hover.setItems({
        'fill': '138 201 38 200',
        'w': 135,
        'h': 55,
        'textSize': 22
    })

    invoerScherm.stop()
    

def draw():
    fill(225,225,225)
    rectMode(CORNER)
    rect(0,0,1080,720)
    for i in range(len(invoerScherm.content)):
        invoerScherm.content[i].draw()
    rectMode(CORNER)
    textAlign(LEFT, BOTTOM)
    dp.draw_player_info()