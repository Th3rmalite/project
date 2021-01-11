import invoerdefinitions as d
from objects import *
import drawPlayers as dp
import eindscherm

def setup(playerList):
    global puntenScherm, toEnd, goBack
    dp.get_players(playerList)
    puntenScherm = Screen('punten', {})
    puntenScherm.start()
    toEnd = Button(None, {
        'x': 980,
        'y': 670,
        'w': 130,
        'h': 50,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '138 201 38 255',
        'placeholder': 'Einde spel',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'font': 'OpenSans-Bold-48.vlw'
    })
    toEnd.hover.setItems({
        'fill': '138 201 38 200',
        'w': 135,
        'h': 55,
        'textSize': 21
    })
    toEnd.goTo = eindscherm
    goBack = Button(None, {
        'x': 90,
        'y': 670,
        'w': 130,
        'h': 50,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '201 138 38 255',
        'placeholder': 'Ga terug',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'font': 'OpenSans-Bold-48.vlw'
    })
    goBack.hover.setItems({
        'fill': '201 138 38 200',
        'w': 135,
        'h': 55,
        'textSize': 21
    })

    puntenScherm.stop()
    

def draw():
    goBack.draw()
    rectMode(CORNER)
    textAlign(LEFT, BOTTOM)
    dp.draw_player_info()