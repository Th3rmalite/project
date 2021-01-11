import objects
import drawPlayers as dp

def setup(playerList):
    dp.get_players(playerList)
    

def draw():
    fill(225,225,225)
    rectMode(CORNER)
    rect(0,0,1080,720)

    dp.draw_player_info()