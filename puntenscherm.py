import invoerdefinitions as d
from objects import *
import drawPlayers as dp

def setup(playerList):
    dp.get_players(playerList)
    invoerScherm = Screen('namen', {})
    invoerScherm.start()
    toEnd = Button(None, {
        'x': 1000,
        'y': 680,
        'w': 130,
        'h': 50,
        'stroke': 'None',
        'fill': d.palette['green']
    })
    invoerScherm.stop()
    

def draw():
    fill(225,225,225)
    rectMode(CORNER)
    rect(0,0,1080,720)
    for i in range(len(invoerScherm.content)):
        invoerScherm.content[i].draw()
    dp.draw_player_info()