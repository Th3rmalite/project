from objects import *
import drawPlayers as dp

def setup(playerList):
    dp.get_players(playerList)
    invoerScherm = Screen('namen', {})
    invoerScherm.start()
    toEnd = Button(None, {
        'x': 1000
    })
    

def draw():
    fill(225,225,225)
    rectMode(CORNER)
    rect(0,0,1080,720)

    dp.draw_player_info()