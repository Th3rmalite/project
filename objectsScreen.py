from objects import *

print(locals())

table = Table({
        'width': '50%',
        'height': '70%',
        'x': '25px',
        'y': '20px',
        'color': color(80,0,0)
    })

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    pass

def draw():
    table.draw()