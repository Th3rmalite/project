import drawPlayers as dp

def setup():
    size(1080,720)
    dp.get_players([("Vincent","black"),("beide Dylans","white"),("beide Dylans","red"),("beide Dylans","blue")])

def draw():
    background(255)
    dp.draw_player_info()

