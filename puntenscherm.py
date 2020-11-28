import drawPlayers as dp

def setup():
    dp.get_players([("Vincent","zwart"),("beide Dylans","wit"),("beide Dylans","rood"),("beide Dylans","blauw")])

def draw():
    background(255)
    dp.draw_player_info()