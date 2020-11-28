import drawPlayers as dp

def setup():
    size(1080,720)
    dp.get_players([("Vincent","zwart"),("beide Dylans","wit"),("beide Dylans","rood"),("beide Dylans","blauw")])

def draw():
    background(255)
    dp.draw_player_info()

