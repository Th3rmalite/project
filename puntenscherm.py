import drawPlayers as dp
from objects import *
#players: [['Dylan', 'white'], ['Vincent', 'black], ['mohammed', 'blue'], ['brent', 'red']]

def setup(playerList):
    dp.get_players(playerList)

def draw():
    background(255)
    dp.draw_player_info()