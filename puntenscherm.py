import drawPlayers as dp

def setup(playerList):
    dp.get_players(playerList)

def draw():
    background(255)
    dp.draw_player_info()